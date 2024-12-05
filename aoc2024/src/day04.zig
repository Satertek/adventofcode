const std = @import("std");
const math = @import("zlm");
const print = std.debug.print;
const day_input = @embedFile("inputs/day04.txt");

const PUZZLE_SIZE: usize = 140;
// example: 10x10
// puzzle: 140x140

fn countXmas(input: []const u8) u8 {
    // Count left-to-right and right-to-left
    if (std.mem.eql(u8, input[0..4], "XMAS") or std.mem.eql(u8, input[0..4], "SAMX")) {
        return 1;
    } else return 0;
}

fn countRow(row: [PUZZLE_SIZE]u8) u32 {
    var count: u32 = 0;
    for (0..PUZZLE_SIZE - 3) |i| {
        count += countXmas(row[i .. i + 4]);
    }
    return count;
}

fn countDiagonals(crossword: [PUZZLE_SIZE][PUZZLE_SIZE]u8) u32 {
    var count: u32 = 0;
    for (0..PUZZLE_SIZE - 3) |i| {
        for (0..PUZZLE_SIZE - 3) |j| {
            const diagonal = [4]u8{ crossword[i][j], crossword[i + 1][j + 1], crossword[i + 2][j + 2], crossword[i + 3][j + 3] };
            count += countXmas(diagonal[0..4]);
        }
    }
    return count;
}

fn countCrossword(crossword: [PUZZLE_SIZE][PUZZLE_SIZE]u8) u32 {
    var count: u32 = 0;

    // Count XMAS left-to-right and right-to-left
    for (crossword) |row| {
        count += countRow(row);
    }

    // Rotate puzzle 90deg
    var rotated: [PUZZLE_SIZE][PUZZLE_SIZE]u8 = undefined;
    for (0..PUZZLE_SIZE) |i| {
        for (0..PUZZLE_SIZE) |j| {
            rotated[j][PUZZLE_SIZE - 1 - i] = crossword[i][j];
        }
    }

    // Count rotated puzzle left-to-right and right-to-left
    for (rotated) |row| {
        count += countRow(row);
    }

    // Count over diagonals (both rotations)
    count += countDiagonals(crossword);
    count += countDiagonals(rotated);

    return count;
}

pub fn main() !void {

    // Split input by newlines and copy each row to crossword
    var crossword: [PUZZLE_SIZE][PUZZLE_SIZE]u8 = .{.{0} ** PUZZLE_SIZE} ** PUZZLE_SIZE;
    var it_row = std.mem.tokenizeScalar(u8, day_input, '\n');
    while (it_row.next()) |row| {
        const j: usize = it_row.index % PUZZLE_SIZE;
        const row_values = row[0..PUZZLE_SIZE].*;
        crossword[j] = row_values;
    }

    var total_count: u32 = 0;

    total_count += countCrossword(crossword);

    print("Count: {}\n", .{total_count});
}
