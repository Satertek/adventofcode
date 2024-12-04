const std = @import("std");
const print = std.debug.print;
const day_input = @embedFile("inputs/day03.txt");

const do_inst_enabled = true; // set true to enable part 2

pub fn main() !void {
    var program_result: i32 = 0;
    var mul_enabled: bool = true;
    var it = std.mem
        .window(u8, day_input, 7, 1);
    find_inst: while (it.next()) |w| {
        //print("{s} {?}\n", .{ w, it.index });
        if (std.mem.eql(u8, w[0..4], "do()")) {
            //print("Found do\n", .{});
            mul_enabled = true;
        }
        if (std.mem.eql(u8, w[0..7], "don't()")) {
            //print("Found don't\n", .{});
            mul_enabled = false;
        }
        if (!mul_enabled and do_inst_enabled) {
            continue :find_inst;
        }
        if (std.mem.eql(u8, w[0..4], "mul(")) {
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
