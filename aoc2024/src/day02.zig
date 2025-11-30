const std = @import("std");
const print = std.debug.print;
const day1_input = @embedFile("inputs/day02.txt");

// MASTER PROBLEM DAMPENER ENABLE SWITCH.  DO NOT TOUCH.
const problem_dampener = true;

fn check_levels(levels: []const u8, problem: u8) bool {
    // Iterate over each value in the line (1 spaces delimeter)
    var is_safe: bool = true;
    var previous_value: i32 = 0;
    var descending: bool = false;
    var ascending: bool = false;
    var values = std.mem.tokenizeScalar(u8, levels, ' ');
    var count: u8 = 0;
    inner: while (values.next()) |value| {
        count += 1;
        const num = std.fmt.parseInt(i32, value, 10) catch |err| {
            std.debug.print("Error in value [{s}] in row [{s}]: {}\n", .{ value, levels, err });
            return false;
        };
        // If the problem dampener has warned us about this value, skip it.
        if (count == problem) {
            continue :inner;
        }
        // Inizialize level on the first value
        if (previous_value == 0) {
            previous_value = num;
            continue :inner;
        }
        // Start checking for bad levels
        if (@abs(num - previous_value) > 3) {
            is_safe = false;
            break :inner;
        }
        if (num - previous_value == 0) {
            is_safe = false;
            break :inner;
        }
        if (num - previous_value > 0) {
            ascending = true;
            if (descending) {
                is_safe = false;
                break :inner;
            }
        }
        if (num - previous_value < 0) {
            descending = true;
            if (ascending) {
                is_safe = false;
                break :inner;
            }
        }
        previous_value = num;
    }
    if (is_safe) {
        if (problem > 0) {
            //print("Problem dampener resolved on [{s}] by skipping position [{d}]\n", .{ levels, problem });
        }
        return true;
    }
    return false;
}

pub fn main() !void {
    // Iterate over each line (newline delimiter)
    var total_safe: i32 = 0;
    var problems_dampened: i32 = 0;
    var data = std.mem.tokenizeScalar(u8, day1_input, '\n');
    while (data.next()) |levels| {
        var is_safe: bool = check_levels(levels, 0);

        // If the levels are not safe, try to dampen the problem
        var problem: u8 = 1;
        dampener: while (!is_safe and problem_dampener) {
            //print("Problem dampener activated on [{s}] at position [{d}]\n", .{ levels, problem });
            is_safe = check_levels(levels, problem);
            if (is_safe) {
                problems_dampened += 1;
                break :dampener;
            }
            if (problem > 10) // Dampener can't count past 10
                break :dampener;
            problem += 1;
        }

        if (is_safe) {
            //print("Line is safe. {s}\n", .{line});
            total_safe += 1;
        }
    }
    print("Total safe lines: {} ({} before {} problems were dampened.)\n", .{ total_safe, (total_safe - problems_dampened), problems_dampened });
}
