from plyer import notification

notification.notify(
    title = '제목입니다.',
    message = '메시지 내용입니다.',
    app_name = "앱 이름",
    # app_icon = 'bluemen_white.ico', # 'C:\\icon_32x32.ico'
    timeout = 10,  # seconds
)