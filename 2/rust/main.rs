fn fibonacci(x: u64) -> u64 {

    if x <= 1 {
        return x;
    } else {
        return fibonacci(x-1) + fibonacci(x-2);
    }
}

fn solve() -> u64{

    let mut sum : u64 = 0;
    let mut value : u64 = 0;
    let mut counter : u64 = 0;

    while value < 4000000 {
        value = fibonacci(counter);
        if value % 2 == 0 {
            sum += value;
        }
        counter += 1;
    }
    return sum;
}

fn main() {

    println!("{}", solve());

}

