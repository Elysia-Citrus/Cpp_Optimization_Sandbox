#include <pybind11/pybind11.h>
#include <cstdlib>
#include <ctime>

// 这里的 namespace py = ... 是为了简写，不然每次都要写 pybind11::
namespace py = pybind11;

// 1. 正常的 C++ 函数，完全不用管 Python 的类型
double calculate_pi_cpp(int iterations) {
    srand(time(NULL));
    int inside_circle = 0;
    for (int i = 0; i < iterations; i++) {
        double x = (double)rand() / RAND_MAX;
        double y = (double)rand() / RAND_MAX;
        if (x * x + y * y <= 1.0) {
            inside_circle++;
        }
    }
    return 4.0 * inside_circle / iterations;
}

// 2. 定义 Python 模块 (这是 pybind11 的魔法)
// 这里的 "Cpp_Optimization_Sandbox" 必须和你的文件名(即项目名)一致！
PYBIND11_MODULE(Cpp_Optimization_Sandbox, m) {
    m.doc() = "This my first pybind11 speeding module"; // 模块文档字符串

    // 将 C++ 函数 calculate_pi_cpp 暴露给 Python，名字叫 calculate_pi
    m.def("calculate_pi", &calculate_pi_cpp, "calulate Pi with mtklsf");
}