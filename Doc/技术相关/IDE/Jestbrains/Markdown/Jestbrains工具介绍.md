# 四种软件介绍

## 🔷 1. PyCharm（Python IDE）

### 📌 简介：

PyCharm 是 JetBrains 专为 Python 开发设计的一款强大 IDE，支持 Django、Flask、FastAPI 等主流框架，也可集成 Jupyter Notebook 和科学计算工具（如 NumPy、Pandas）。

### 🌟 主要特点：

- 智能代码补全与导航
- 内置调试器和单元测试
- 支持虚拟环境与包管理（pip/conda）
- Jupyter Notebook 支持
- Git 等版本控制集成
- 数据库工具集成（专业版）

### 🛠️ 基础使用：

1. 创建项目：启动 PyCharm → New Project → 选择解释器（推荐使用虚拟环境）
2. 编写代码：`.py` 文件中进行开发，支持语法高亮和错误提示
3. 运行程序：右键文件 → Run
4. 调试程序：打断点 → 右键 → Debug
5. 安装库：File → Settings → Python Interpreter → "+" 添加依赖
6. 使用终端：View → Tool Windows → Terminal 打开命令行

------

## 🔷 2. WebStorm（前端开发 IDE）

### 📌 简介：

WebStorm 是一款专注于 JavaScript、TypeScript 和现代前端框架（如 React、Vue、Angular）的专业 IDE。

### 🌟 主要特点：

- 强大的代码补全和重构功能
- 支持 HTML/CSS/JS/TS 等语言
- 支持 Node.js、Vue、React、Next.js、Nuxt.js 等框架
- 内置调试工具、测试工具（Jest、Mocha）
- Git、GitHub、npm 集成
- 支持 ESLint、Prettier 等前端工具

### 🛠️ 基础使用：

1. 创建项目：启动 WebStorm → New Project → 选择框架模板或空项目
2. 安装依赖：使用内置终端 `npm install` 或 `yarn`
3. 编写代码：支持语法高亮、智能提示、组件跳转
4. 运行调试：Run → Edit Configurations 添加运行脚本
5. 使用版本控制：VCS → Git 初始化仓库，支持 GitHub

------

## 🔷 3. IntelliJ IDEA（Java 全能 IDE）

### 📌 简介：

IntelliJ IDEA 是 JetBrains 最著名的产品，广泛用于 Java 开发，也支持 Kotlin、Scala、Groovy、Spring、Maven、Gradle 等。

### 🌟 主要特点：

- 支持 Java/Kotlin 等 JVM 语言
- Spring、Spring Boot 深度支持
- 强大的 Maven/Gradle 项目管理
- 数据库、HTTP 客户端内置
- 支持后端 + Web 开发（高级版可整合前端框架）

### 🛠️ 基础使用：

1. 创建项目：New Project → Java 或 Spring Boot
2. 管理依赖：选择 Maven/Gradle，编辑 `pom.xml` 或 `build.gradle`
3. 编写代码：提供类模板、代码导航、智能补全
4. 运行程序：右键类文件 → Run 或使用 Shift+F10
5. 调试程序：添加断点 → Debug
6. 查看数据库：右侧 Database 工具窗口连接数据库（高级版）

------

## 🔷 4. CLion（C/C++ 专业 IDE）

### 📌 简介：

CLion 是一款用于 C/C++ 开发的跨平台 IDE，支持 CMake、Makefile、GDB、LLDB，适合系统开发、嵌入式开发等场景。

### 🌟 主要特点：

- CMake 支持（核心项目构建系统）
- 内置 GDB/LLDB 调试器
- 支持 C/C++17/20、CUDA、Assembly
- 集成 Valgrind、Google Test、Catch2 等工具
- 智能补全与代码导航、重构支持

### 🛠️ 基础使用：

1. 创建项目：New Project → C/C++ Executable → 选择模板
2. 编写代码：`.cpp/.h` 文件编写逻辑，支持语法检查和提示
3. 构建项目：使用 CMake 自动构建
4. 运行程序：点击运行按钮或右键 → Run
5. 调试程序：设置断点后点击 Debug
6. 安装工具链：File → Toolchains 配置 gcc/g++、CMake、Debugger 路径

------

## 🧩 JetBrains 通用功能（以上 IDE 通用）：

| 功能             | 快捷键（Windows）       | 快捷键（macOS）       |
| ---------------- | ----------------------- | --------------------- |
| 全局搜索         | `Ctrl+Shift+F`          | `Cmd+Shift+F`         |
| 查找类/文件/符号 | `Ctrl+N / Ctrl+Shift+N` | `Cmd+O / Cmd+Shift+O` |
| 自动补全         | `Ctrl+Space`            | `Ctrl+Space`          |
| 运行             | `Shift+F10`             | `Ctrl+R`              |
| 调试             | `Shift+F9`              | `Ctrl+D`              |
| 终端             | `Alt+F12`               | `Alt+F12`             |
| 格式化代码       | `Ctrl+Alt+L`            | `Cmd+Option+L`        |



# 好用的插件

## 🔌 一、通用高效插件（适用于大部分 JetBrains IDE）

### 1. **Key Promoter X**

- 📌 作用：教你快捷键，用鼠标点击功能时提示对应快捷键。
- 👍 适合刚开始学习 IDE 的新手，大大提升操作效率。

------

### 2. **Rainbow Brackets**

- 📌 作用：为成对的括号添加彩虹颜色，提升代码结构可读性。
- 👍 支持多语言，如 Python、Java、C++、JavaScript 等。

------

### 3. **CodeGlance Pro**

- 📌 作用：在右侧添加代码缩略图导航（像 VSCode 的 minimap）。
- 👍 长文件定位非常方便。

------

### 4. **Material Theme UI**

- 📌 作用：美化界面，提供多种 UI 主题和图标风格。
- ✨ 搭配 One Dark / Dracula / GitHub Dark 很有现代感。

------

### 5. **.ignore**

- 📌 作用：支持 `.gitignore`、`.dockerignore` 等文件的语法高亮与模板。
- 👍 方便快速添加和维护忽略文件。

------

### 6. **Presentation Assistant**

- 📌 作用：实时展示你按下的快捷键，适合教学或演示。

------

### 7. **Translation (Google Translate)**

- 📌 作用：鼠标选中英文代码注释/文档 → 快速翻译为中文。
- 🌍 支持双向翻译，适合英文不熟练的开发者。

------

## 🌐 二、WebStorm / IDEA 前端开发常用插件

### 8. **Vue.js / Angular / React Plugin**

- 📌 作用：提供对应框架的语法支持、代码补全、模板提示。
- 🔧 WebStorm 已内置，IDEA 需要单独安装。

------

### 9. **Tailwind CSS**

- 📌 作用：支持 Tailwind CSS 智能补全、类名预览、颜色显示。
- 👌 前端写样式神器。

------

### 10. **Prettier**

- 📌 作用：代码自动格式化插件，配合 `.prettierrc` 使用。
- ✨ 强烈推荐前端项目统一格式化规则使用。

------

### 11. **Node.js**

- 📌 作用：为 Node.js 开发提供调试、运行和自动补全支持。
- ✅ 如果你用 WebStorm 开发后端 Node 项目，必装。

------

## 🧪 三、PyCharm Python 开发插件

### 12. **Python Docstring Generator**

- 📌 作用：自动生成函数的 docstring 文档注释（支持 Google、Sphinx 等格式）。
- 📝 提升代码可读性与文档质量。

------

### 13. **Kite / TabNine（AI 补全）**

- 📌 作用：AI 驱动的智能代码补全，适合提升代码编写效率。
- ⚠️ 注意隐私问题，选择你信任的服务。

------

## 💻 四、CLion / C++ 开发增强插件

### 14. **CMake Plus**

- 📌 作用：增强 CMake 文件的语法高亮、跳转、快速导航。

------

### 15. **Valgrind Memcheck Integration**

- 📌 作用：集成 Valgrind，进行内存泄漏检查。
- 🛡️ 对嵌入式或底层系统开发非常有用。

------

## ☁️ 五、版本控制 / 协作工具插件

### 16. **GitToolBox**

- 📌 作用：在编辑器状态栏中显示当前 Git 分支、作者、最近提交。
- 👍 支持 Git blame 提示，方便团队协作。

------

### 17. **GitHub Copilot (付费)**

- 📌 作用：AI 自动补全整段代码（OpenAI 支持），强大但需订阅。
- ⚠️ 推荐使用于非敏感项目。