const std = @import("std");
const print = std.debug.print;
const day1_input = @embedFile("inputs/day1.txt");

pub fn main() !void {
    // Prints to stderr (it's a shortcut based on `std.io.getStdErr()`)
    std.debug.print("All your {s} are belong to us.\n", .{"codebase"});

    // stdout is for the actual output of your application, for example if you
    // are implementing gzip, then only the compressed bytes should be sent to
    // stdout, not any debugging messages.
    const stdout_file = std.io.getStdOut().writer();
    var bw = std.io.bufferedWriter(stdout_file);
    const stdout = bw.writer();

    try stdout.print("Testing...", .{});

    try day1();

    try bw.flush(); // don't forget to flush!
}

pub fn day1() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    const allocator = gpa.allocator();

    var data = std.mem.tokenizeScalar(u8, day1_input, '\n');
    var left_list = std.ArrayList(i32).init(allocator);
    defer left_list.deinit();
    var right_list = std.ArrayList(i32).init(allocator);
    defer right_list.deinit();
    var count: u16 = 0;
    // Iterate over each line
    while (data.next()) |line| {
        var values = std.mem.tokenizeSequence(u8, line, "   ");
        var is_first = true;
        // Iterator over each value in the line
        while (values.next()) |value| {
            const num = std.fmt.parseInt(i32, value, 10) catch |err| {
                std.debug.print("Failed to parse number: {}\n", .{err});
                continue;
            };
            if (is_first) {
                try left_list.append(num);
                is_first = false;
            } else {
                try right_list.append(num);
            }
        }
        count += 1;
    }

    // Sort lists in ascending order
    std.mem.sort(i32, left_list.items, {}, std.sort.asc(i32));
    std.mem.sort(i32, right_list.items, {}, std.sort.asc(i32));

    // Loop over sorted lists and calculate the total distance
    var total_distance: u32 = 0;
    while (left_list.getLastOrNull() != null) {
        total_distance += @abs(left_list.pop() - right_list.pop());
    }

    print("Total distance: {}\n", .{total_distance});
}
