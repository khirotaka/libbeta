use pyo3::prelude::*;

#[pyfunction]
fn rust_func(a: i32) -> i32 {
    a * a
}

#[pyfunction]
fn add(a: i32, b: i32) -> i32 {
    a + b
}