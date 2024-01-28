use std::{io, process::exit};

fn convert_f(fahrenheit:f64) -> f64 {
    (fahrenheit - 32.0) / 1.8
} 

fn convert_c(celsius:f64) -> f64 {
    (celsius * 1.8) + 32.0
}

fn main() {
    println!("\n Hello, world!");
    println!("\n Type F - Convert from fahrenheit to celsius");
    println!("\n Type C - Convert from celsius to fahreinheit");
    println!("\n press ctrl + c to exit or type anything");
    println!("(F/C/N)");
    let mut user_input:String = String::new();  

    io::stdin()
        .read_line(&mut user_input)
        .expect("Failed to take user input");
    

    match user_input.trim().to_lowercase().as_str() {
        "f" => {
            println!("Enter the Fahrenheit temprature to be converted:");
            let mut n: String = String::new();
            io::stdin()
                .read_line(&mut n)
                .expect("Failed to take user input");
            
            let temp: f64 = match n.trim().parse() {
                Ok(num) => num,
                Err(_) => exit(1),
            };
            let conversion_result: f64 = convert_f(temp);
            println!("{conversion_result}");
            println!("Conversion success!")
        },

        "c" => {
            println!("Enter the Celsius temprature to be converted:");
            let mut n: String = String::new();
            io::stdin()
                .read_line(&mut n)
                .expect("Failed to take user input");
            
            let temp: f64 = match n.trim().parse() {
                Ok(num) => num,
                Err(_) => exit(1),
            };
            let conversion_result: f64 = convert_c(temp);
            println!("{conversion_result}");
            println!("Conversion success!")       
        }

        _ => println!("Bye!")

    };

}


