use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

mod funcs;
use funcs::*;


#[pymodule]
fn rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(rust_func))?;
    Ok(())
}

#[pymodule]
fn utils(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(add))?;
    Ok(())
}
