fn solve(mut n : u64) -> u64 {
    let mut i : u64 = 2;

    while i*i <= n{
        if n % i != 0 {
            i += 1;
        }else {
            n = n/i;
        }
    }
    return n;
}

fn main(){
    println!("{}", solve(600851475143));
}

