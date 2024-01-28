use std::env;
use std::process;
use minigrep_tut::Config;

fn main() {
    let args: Vec<String> = env::args().collect();
    let config = Config::build(&args).unwrap_or_else(|err| {
        println!("Problem parsing arguments: {err}"); // Execute if error
        std::process::exit(1);
    });

    println!("Searching for {}", config.query);
    println!("In file {}:\n", config.file_path);

    if let Err(e) = minigrep_tut::run(config) { // Execute if error
        println!("Application error: {e}");
        process::exit(1);
    }
}