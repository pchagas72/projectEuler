fn solve() -> i32 {
    let mut sum : i32 = 0;
    for i in 0 .. 1000 {
        if i % 3 == 0 || i % 5 == 0 {
            sum += i;
        }
    }
    return sum;
}

fn main() {
    println!("{}", solve());
}
