use std::f64::consts::PI;

struct Map {
    map: Vec<Vec<char>>,
    centerx: f64,
    centery: f64,
}

impl Map {
    fn new(width: i32, height: i32) -> Self {
        let mut map = vec![];
        for _row in 0..width {
            let mut column = vec![];
            for _column_item in 0..height {
                column.push('#');
            }
            map.push(column);
        }
        Self {
            map: map,
            centerx: width as f64 / 2.0,
            centery: height as f64 / 2.0,
        }
    }

    fn write_char(&mut self, location: (usize, usize), new_char: char) {
        let row = self.map.get_mut(location.1);
        match row { // Check if row exists
            None => {}
            Some(test) => {
                if location.0 < test.len() { // Check if it is within the bounds of x-axis
                    test[location.0] = new_char; // Check if its in bound
                }
            }
        }
    }

    fn print_map(&self) {
        for row in &self.map {
            println!("{}", String::from_iter(row));
        }
    }

    fn draw_polar_function(&mut self, rotations: i32, p: &dyn Fn(f64) -> f64, character: char) {
        let degree = rotations * 360;
        for deg in 0..degree {
            let theta: f64 = (deg as f64).to_radians(); // Reduce scale
            let radius = p(theta); // p of theta
            let (x, y) = cartesian(theta, radius);
            self.write_char((self.correct_x(x), self.correct_y(y)), character); // Place Char
        }
    }

    fn draw_function(&mut self, start: i32, end: i32, f: &dyn Fn(f64) -> f64, character: char) {
        for x in start..end+1 {
            let y: f64 = f(x.into());
            self.write_char((self.correct_x(x.into()), self.correct_y(y)), character); // Place Char
        }
    }

    fn correct_y(&self, y: f64) -> usize{
        (-y + self.centery) as usize // inverted centered y
    }

    fn correct_x(&self, x:f64) -> usize {
        (x + (self.centerx - 1.0)).round() as usize // centered x
    }
}


fn cartesian(theta: f64, radius: f64) -> (f64, f64) {
    (radius * theta.cos(), radius * theta.sin()) // X, Y in cartesian
}

fn golden_fun(theta: f64) -> f64 {
    (1.618033988749 as f64).powf((2.0 * theta) / PI) // golden ratio spiral
}

fn equals(x: f64) -> f64 {
    x
}

fn sine(x: f64) -> f64 {
    x.sin()
}

fn main() {
    let mut test = Map::new(75, 75);
    test.draw_function(-10, 50, &equals, '[');
    test.draw_function(-10, 50, &sine, 'P');
    test.draw_polar_function(1, &golden_fun , '&');
    test.print_map();
}
