#include <cstdlib> // 包含 rand()
#include <ctime>   // 包含 time()

// 这里的 extern "C" __declspec(dllexport)告诉编译器：“把这个函数名字暴露出去，让外面的 Python 能找到它”
extern "C" __declspec(dllexport) double calculate_pi(int iterations) {

    // 初始化随机数种子（为了简单，这里用基础的 rand）
    // 在生产环境中通常会用更高级的随机数生成器
    srand(time(NULL));

    int inside_circle = 0;

    for (int i = 0; i < iterations; i++) {
        // 生成 0 到 1 之间的随机坐标 (x, y)
        // rand() 返回 0 到 RAND_MAX，除以 RAND_MAX 得到 0.0~1.0
        double x = (double)rand() / RAND_MAX;
        double y = (double)rand() / RAND_MAX;

        // 判断是否落在圆内 (x^2 + y^2 <= 1)
        if (x * x + y * y <= 1.0) {
            inside_circle++;
        }
    }

    // 蒙特卡洛公式：Pi = 4 * (圆内点数 / 总点数)
    return 4.0 * inside_circle / iterations;
}