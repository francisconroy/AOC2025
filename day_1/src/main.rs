use std::fs::File;
use std::io::{self, BufRead};
use std::ops::Add;
use std::path::Path;

const MAX_VALUE: i8 = 99i8;

fn main() {
    // File hosts.txt must exist in the current path
    if let Ok(lines) = read_lines("./input.txt") {
        // Consumes the iterator, returns an (Optional) String
        let mut position = 0i8;
        let mut password = 0;
        for line in lines.map_while(Result::ok) {
            let direction = line.chars().nth(0).unwrap();
            let count_string = line[1..].to_string();
            let count = count_string.parse::<usize>().unwrap();
            let increment = if direction.eq(&'L') { -1i8 } else { 1i8 };

            for _ in 0..count {
                position = position.add(increment as i8);
                if position >= MAX_VALUE {
                    position = 0
                } else if position < 0 {
                    position = MAX_VALUE
                };
            }

            if position == 0 {
                password += 1
            };
            println!("{}", password);
        }
    }
}

// The output is wrapped in a Result to allow matching on errors.
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
