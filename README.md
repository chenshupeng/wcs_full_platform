这个仓库 wcs_full_platform 是一个关于仓储控制系统（WCS）的仿真平台，主要用于仓储系统的模拟和研究。以下是对仓库内容的详细介绍：
主要功能模块
任务管理：通过 TaskManager 类来管理任务。该类包含了任务的初始化、自动模拟循环、添加任务和获取统计信息等功能。
用户界面：使用 PyQt5 库创建了用户界面，包括主窗口 MainWindow 和控制面板 ControlPanel。主窗口显示了 3D 视图，控制面板包含一个刷新任务的按钮。
服务器：使用 Flask 框架创建了一个服务器，用于处理与任务管理相关的请求。
模拟数据：仓库中包含一个 mock_data.json 文件，提供了一些模拟的 SKU 数据。
配置文件：config.py 文件包含了一些系统配置信息，如区域数量、SKU 数量、波次托盘数量和运输时间等。
