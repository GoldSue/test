from apscheduler.schedulers.blocking import BlockingScheduler
from win10toast import ToastNotifier

# 你的任务函数
def show_notification():
    toaster = ToastNotifier()
    toaster.show_toast(
        "提醒通知",  # 通知标题
        "这是一个每分钟通知的示例。",  # 通知内容
        icon_path=None,  # 图标路径（可选）
        duration=10  # 持续时间（秒）
    )

# 创建调度器
scheduler = BlockingScheduler()

# 添加定时任务，每分钟执行一次
scheduler.add_job(show_notification, 'interval', minutes=1)

# 启动调度器
scheduler.start()
