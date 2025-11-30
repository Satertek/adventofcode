const std = @import("std");
const print = std.debug.print;
const day_input = @embedFile("inputs/day03.txt");

const do_inst_enabled = true; // set true to enable part 2

fn isDigit(val: u8) bool {
    return val >= '0' and val <= '9';
}

pub fn main() !void {
    var program_result: i32 = 0;
    var mul_enabled: bool = true;

    var it = std.mem.window(u8, day_input, 7, 1);

    find_inst: while (it.next()) |w| {
        // If do/don't instruction are enabled, check for instruction
        if (do_inst_enabled) {
            if (std.mem.eql(u8, w[0..4], "do()")) {
                mul_enabled = true;
            } else if (std.mem.eql(u8, w[0..7], "don't()")) {
                mul_enabled = false;
            }
        }

        // Skip mul instruction check if multiplication is disabled
        if (!mul_enabled) {
            continue :find_inst;
        }

        // Process multiplication instruction
        if (std.mem.eql(u8, w[0..4], "mul(")) {
            const i = (it.index orelse 0) + 3;
            var itn = std.mem.window(u8, day_input[i..day_input.len], 1, 1);

            var mult_one: i32 = 0;
            var mult_two: i32 = 0;
            var val_slice: []const u8 = itn.next() orelse continue :find_inst;
            var val = val_slice[0];

            // First digit
            if (!isDigit(val)) continue :find_inst;
            mult_one = val - '0';

            // Optional second digit
            val_slice = itn.next() orelse continue :find_inst;
            val = val_slice[0];
            if (isDigit(val)) {
                mult_one = mult_one * 10 + (val - '0');
                val_slice = itn.next() orelse continue :find_inst;
                val = val_slice[0];
            }

            // Optional third digit
            if (val != ',' and isDigit(val)) {
                mult_one = mult_one * 10 + (val - '0');
                val_slice = itn.next() orelse continue :find_inst;
                val = val_slice[0];
            }

            // Comma
            if (val == ',') {
                val_slice = itn.next() orelse continue :find_inst;
                val = val_slice[0];
            }

            // First Digit
            if (!isDigit(val)) continue :find_inst;
            mult_two = val - '0';

            // Optional second digit
            val_slice = itn.next() orelse continue :find_inst;
            val = val_slice[0];
            if (isDigit(val)) {
                mult_two = mult_two * 10 + (val - '0');
                val_slice = itn.next() orelse continue :find_inst;
                val = val_slice[0];
            }

            // Optional third digit
            if (val != ')' and isDigit(val)) {
                mult_two = mult_two * 10 + (val - '0');
                val_slice = itn.next() orelse continue :find_inst;
                val = val_slice[0];
            }

            // Calculate result if we found a complete multiplication
            if (val == ')') {
                program_result += mult_one * mult_two;
            }
        }
    }

    print("Program result: {d}\n", .{program_result});
}
