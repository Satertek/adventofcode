const std = @import("std");
const print = std.debug.print;
const day_input = @embedFile("inputs/day03.txt");

pub fn main() !void {
    var program_result: i32 = 0;

    var it = std.mem
        .window(u8, day_input, 4, 1);
    find_inst: while (it.next()) |w| {
        //print("{s} {?}\n", .{ w, it.index });
        if (std.mem.eql(u8, w, "mul(")) {
            //print("Found mul\n", .{});
            const i = (it.index orelse 0) + 3;
            var itn = std.mem.window(u8, day_input[i..day_input.len], 1, 1);

            var mult_one: i32 = 0;
            var mult_two: i32 = 0;

            var val_slice: []const u8 = itn.next() orelse continue :find_inst;
            var val = val_slice[0];
            //print("First value: {d}\n", .{val});
            if (val > 47 and val < 58) { // if we have a digit
                mult_one = val - 48;
                //print("Found digit: {d}\n", .{mult_one});
            } else {
                continue :find_inst;
            }

            // this should be a digit or a comma
            val_slice = itn.next() orelse continue :find_inst;
            val = val_slice[0];
            //print("Second value: {d}\n", .{val});
            if (val > 47 and val < 58) {
                mult_one = mult_one * 10 + val - 48;
                //print("Modified digit: {d}\n", .{mult_one});
            } else if (val != ',') {
                continue :find_inst;
            }

            if (val != ',') {
                val_slice = itn.next() orelse continue :find_inst;
                val = val_slice[0];
                //print("Second value: {d}\n", .{val});
                if (val > 47 and val < 58) {
                    mult_one = mult_one * 10 + val - 48;
                    //print("Modified digit: {d}\n", .{mult_one});
                } else if (val != ',') {
                    continue :find_inst;
                }
            }

            val_slice = itn.next() orelse continue :find_inst;
            val = val_slice[0];
            //print("Third value: {d}\n", .{val});
            if (val == ',') {
                val_slice = itn.next() orelse continue :find_inst;
                val = val_slice[0];
                //print("Fourth value: {d}\n", .{val});
            }

            if (val > 47 and val < 58) {
                mult_two = val - 48;
                //print("Found digit: {d}\n", .{mult_one});
            } else {
                continue :find_inst;
            }

            val_slice = itn.next() orelse continue :find_inst;
            val = val_slice[0];
            //print("Fifth value: {d}\n", .{val});
            if (val > 47 and val < 58) {
                mult_two = mult_two * 10 + val - 48;
                //print("Modified digit: {d}\n", .{mult_one});
            }

            if (val != ')') {
                val_slice = itn.next() orelse continue :find_inst;
                val = val_slice[0];
                //print("Fifth value: {d}\n", .{val});
                if (val > 47 and val < 58) {
                    mult_two = mult_two * 10 + val - 48;
                    //print("Modified digit: {d}\n", .{mult_one});
                }
            }

            if (val != ')') {
                val_slice = itn.next() orelse continue :find_inst;
                val = val_slice[0];
                //print("Sixth value: {d}\n", .{val});
            }

            if (val == ')') {
                program_result += mult_one * mult_two;
                //print("Mutliplying {d} by {d} = {d}\n", .{ mult_one, mult_two, program_result });
            }
        }
    }
    print("Program result: {d}\n", .{program_result});
}
