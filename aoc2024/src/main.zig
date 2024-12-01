const std = @import("std");
const print = std.debug.print;
const day1_input = @embedFile("inputs/day1.txt");

pub fn main() !void {
    try day1();
}

pub fn day1() !void {

    // Parse our input data into two arrays (left and right)
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    const allocator = gpa.allocator();
    var data = std.mem.tokenizeScalar(u8, day1_input, '\n');
    var left_list = std.ArrayList(i32).init(allocator);
    defer left_list.deinit();
    var right_list = std.ArrayList(i32).init(allocator);
    defer right_list.deinit();

    // Iterate over each line (newline delimiter)
    while (data.next()) |line| {
        var values = std.mem.tokenizeSequence(u8, line, "   ");
        var is_first = true;
        // Iterator over each value in the line (3 spaces delimiter)
        while (values.next()) |value| {
            const num = std.fmt.parseInt(i32, value, 10) catch |err| {
                std.debug.print("I AM ERROR: {}\n", .{err});
                continue;
            };
            if (is_first) {
                try left_list.append(num);
                is_first = false;
            } else {
                try right_list.append(num);
            }
        }
    }

    // Sort lists in ascending order
    std.mem.sort(i32, left_list.items, {}, std.sort.asc(i32));
    std.mem.sort(i32, right_list.items, {}, std.sort.asc(i32));

    // Set up hash map for our similarity score
    var similarity_hashmap = std.AutoHashMap(i32, i32).init(allocator);
    defer similarity_hashmap.deinit();

    const saved_left_list = left_list.items;

    // Loop over sorted lists and calculate the total distance
    var total_distance: u32 = 0;
    while (left_list.getLastOrNull() != null) {
        const left: i32 = left_list.pop();
        const right: i32 = right_list.pop();
        total_distance += @abs(left - right);

        // Put the right value in a hashmap, and increment count of that value
        const previous_value = similarity_hashmap.get(right) orelse 0;
        try similarity_hashmap.put(right, previous_value + 1);
    }

    // Loop over the left list again for similarity score
    var similarity_score: i32 = 0;
    for (saved_left_list) |left| {
        similarity_score += left * (similarity_hashmap.get(left) orelse 0);
    }

    print("Day 1:\nTotal distance: {}\n", .{total_distance});
    print("Total similiarity: {}\n", .{similarity_score});
}
