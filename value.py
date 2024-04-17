# 表单
content1 = {
    "config": {},
    "i18n_elements": {
        "zh_cn": [
            {
                "tag": "action",
                "actions": [
                    {
                        "tag": "input",
                        "placeholder": {"tag": "plain_text", "content": "请输入名字"},
                        "default_value": "",
                        "width": "default",
                    }
                ],
                "fallback": {
                    "tag": "fallback_text",
                    "text": {
                        "tag": "plain_text",
                        "content": "仅支持在 V6.8 及以上版本使用",
                    },
                },
            },
            {
                "tag": "action",
                "actions": [
                    {
                        "tag": "select_static",
                        "placeholder": {"tag": "plain_text", "content": "请选择选项"},
                        "options": [
                            {
                                "text": {"tag": "plain_text", "content": "选项1"},
                                "value": "1",
                                "icon": {
                                    "tag": "standard_icon",
                                    "token": "signature_outlined",
                                },
                            },
                            {
                                "text": {"tag": "plain_text", "content": "选项2"},
                                "value": "2",
                                "icon": {
                                    "tag": "standard_icon",
                                    "token": "signature_outlined",
                                },
                            },
                        ],
                        "type": "default",
                        "width": "default",
                    }
                ],
            },
            {
                "tag": "action",
                "actions": [
                    {
                        "tag": "date_picker",
                        "placeholder": {"tag": "plain_text", "content": "请选择时间"},
                        "width": "default",
                    }
                ],
            },
            {
                "tag": "action",
                "actions": [
                    {
                        "tag": "picker_time",
                        "placeholder": {"tag": "plain_text", "content": "请选择"},
                        "width": "default",
                    }
                ],
            },
            {
                "tag": "action",
                "actions": [
                    {
                        "tag": "picker_datetime",
                        "placeholder": {"tag": "plain_text", "content": "请选择日期"},
                        "width": "default",
                    }
                ],
            },
            {
                "tag": "action",
                "actions": [
                    {
                        "tag": "select_person",
                        "placeholder": {"tag": "plain_text", "content": "请选择"},
                        "options": [],
                        "width": "default",
                        "type": "default",
                    }
                ],
            },
            {
                "tag": "form",
                "elements": [
                    {
                        "tag": "column_set",
                        "flex_mode": "none",
                        "background_style": "default",
                        "horizontal_spacing": "8px",
                        "horizontal_align": "left",
                        "columns": [
                            {
                                "tag": "column",
                                "width": "auto",
                                "vertical_align": "top",
                                "vertical_spacing": "8px",
                                "background_style": "default",
                                "elements": [
                                    {
                                        "tag": "button",
                                        "text": {
                                            "tag": "plain_text",
                                            "content": "提交",
                                        },
                                        "type": "primary",
                                        "complex_interaction": True,
                                        "action_type": "form_submit",
                                        "name": "Button_luv3v13b",
                                    }
                                ],
                            },
                            {
                                "tag": "column",
                                "width": "auto",
                                "vertical_align": "top",
                                "vertical_spacing": "8px",
                                "background_style": "default",
                                "elements": [
                                    {
                                        "tag": "button",
                                        "text": {
                                            "tag": "plain_text",
                                            "content": "取消",
                                        },
                                        "type": "default",
                                        "complex_interaction": True,
                                        "action_type": "form_reset",
                                        "name": "Button_luv3v13c",
                                    }
                                ],
                            },
                        ],
                        "margin": "0px 0px 0px 0px",
                    }
                ],
                "name": "Form_luv3v13a",
                "fallback": {
                    "tag": "fallback_text",
                    "text": {
                        "tag": "plain_text",
                        "content": "仅支持在 V6.6 及以上版本使用",
                    },
                },
            },
        ]
    },
    "i18n_header": {
        "zh_cn": {
            "title": {"tag": "plain_text", "content": "{Form容器所有能力"},
            "subtitle": {"tag": "plain_text", "content": "示例文本"},
            "template": "blue",
        }
    },
}

# 能力卡片
content2 = {
    "config": {},
    "i18n_elements": {
        "zh_cn": [
            {
                "tag": "column_set",
                "flex_mode": "none",
                "horizontal_spacing": "default",
                "background_style": "default",
                "columns": [
                    {
                        "tag": "column",
                        "elements": [
                            {
                                "tag": "div",
                                "text": {
                                    "tag": "plain_text",
                                    "content": "我可以帮助你完成不同场景下的任务，快试试吧！",
                                    "text_size": "normal",
                                    "text_align": "left",
                                    "text_color": "default",
                                },
                            }
                        ],
                        "width": "weighted",
                        "weight": 1,
                    }
                ],
            },
            {
                "tag": "column_set",
                "flex_mode": "none",
                "background_style": "default",
                "horizontal_spacing": "8px",
                "horizontal_align": "left",
                "columns": [
                    {
                        "tag": "column",
                        "width": "weighted",
                        "vertical_align": "top",
                        "vertical_spacing": "8px",
                        "background_style": "default",
                        "elements": [
                            {
                                "tag": "button",
                                "text": {"tag": "plain_text", "content": "Chat Data"},
                                "type": "default",
                                "complex_interaction": True,
                                "width": "fill",
                                "size": "medium",
                            }
                        ],
                        "weight": 1,
                    },
                    {
                        "tag": "column",
                        "width": "weighted",
                        "vertical_align": "top",
                        "vertical_spacing": "8px",
                        "background_style": "default",
                        "elements": [
                            {
                                "tag": "button",
                                "text": {"tag": "plain_text", "content": "Chat Excel"},
                                "type": "default",
                                "complex_interaction": True,
                                "width": "fill",
                                "size": "medium",
                            }
                        ],
                        "weight": 1,
                    },
                    {
                        "tag": "column",
                        "width": "weighted",
                        "vertical_align": "top",
                        "vertical_spacing": "8px",
                        "background_style": "default",
                        "elements": [
                            {
                                "tag": "button",
                                "text": {"tag": "plain_text", "content": "Chat  DB"},
                                "type": "default",
                                "complex_interaction": True,
                                "width": "fill",
                                "size": "medium",
                            }
                        ],
                        "weight": 1,
                    },
                ],
                "margin": "16px 0px 0px 0px",
            },
            {
                "tag": "column_set",
                "flex_mode": "none",
                "background_style": "default",
                "horizontal_spacing": "8px",
                "horizontal_align": "left",
                "columns": [
                    {
                        "tag": "column",
                        "width": "weighted",
                        "vertical_align": "top",
                        "elements": [
                            {
                                "tag": "button",
                                "text": {
                                    "tag": "plain_text",
                                    "content": "Chat Knowelage",
                                },
                                "type": "default",
                                "complex_interaction": True,
                                "width": "fill",
                                "size": "medium",
                            }
                        ],
                        "weight": 1,
                    },
                    {
                        "tag": "column",
                        "width": "weighted",
                        "vertical_align": "top",
                        "elements": [
                            {
                                "tag": "button",
                                "text": {"tag": "plain_text", "content": "DashBoard"},
                                "type": "default",
                                "complex_interaction": True,
                                "width": "fill",
                                "size": "medium",
                            }
                        ],
                        "weight": 1,
                    },
                    {
                        "tag": "column",
                        "width": "weighted",
                        "vertical_align": "top",
                        "elements": [
                            {
                                "tag": "button",
                                "text": {"tag": "plain_text", "content": "Agent"},
                                "type": "default",
                                "complex_interaction": True,
                                "width": "fill",
                                "size": "medium",
                            }
                        ],
                        "weight": 1,
                    },
                ],
                "margin": "16px 0px 0px 0px",
            },
        ]
    },
    "i18n_header": {
        "zh_cn": {
            "title": {
                "tag": "plain_text",
                "content": "您好，我是销售助理，我能帮您做些什么吗？",
            },
            "subtitle": {"tag": "plain_text", "content": ""},
            "template": "default",
        }
    },
}

# 可折叠表单
content3 = {
    "config": {},
    "i18n_elements": {
        "zh_cn": [
            {
                "tag": "markdown",
                "content": "CRM系统，即客户关系管理系统（Customer Relationship Management），是一种旨在帮助企业更好地管理与客户相关的互动和关系的商业策略。它通过信息化手段，整合企业内部资源，优化业务流程，提高客户满意度和忠诚度，从而增加企业的销售收入和市场份额。CRM系统的核心在于客户信息的集中管理、销售过程的跟踪与优化、市场营销活动的执行与分析、以及售后服务的高效处理。\nCRM系统通常包含以下几个主要功能模块：\n1. 客户信息管理15：将客户的基本信息、交易历史、沟通记\n2. 标准emoji 😁😢🌞💼🏆❌✅\n飞书emoji :OK::THUMBSUP:\n3. *斜体***粗体**~~删除线~~<font color='red'>这是红色文本</font>[文字链接](https:#open.feishu.cn/document/server-docs/im-v1/message-reaction/emojis-introduce)<at id=all></at>\n\\n ---\\n\n:Emoji Key:\n\n",
                "text_align": "left",
                "text_size": "normal",
            },
            {"tag": "hr"},
            # {
            #     "tag": "markdown",
            #     "content": "**参考**\n[1][什么是CRM系统？它的作用是什么？ - 知乎](https:#open.feishu.cn/document/server-docs/im-v1/message-reaction/emojis-introduce)\n[2][什么是 CRM？| Oracle 中国](https:#open.feishu.cn/document/server-docs/im-v1/message-reaction/emojis-introduce)\n[3][CRM系统的整体功能设计 | 人人都是产品经理](https:#open.feishu.cn/document/server-docs/im-v1/message-reaction/emojis-introduce)\n[3][高品质开源商城系统-CRMEB官网](https:#open.feishu.cn/document/server-docs/im-v1/message-reaction/emojis-introduce)",
            #     "text_align": "left",
            #     "text_size": "notation",
            # },
            {
                "tag": "collapsible_panel",  # 折叠面板的标签。
                "expanded": True,  # 面板是否展开。默认值 false。
                "background_color": "grey",  # 折叠面板的背景色，默认为透明
                "header": {
                    # 折叠面板的标题设置。
                    "title": {
                        # 标题文本设置。支持 plain_text 和 markdown。
                        "tag": "markdown",
                        "content": "**参考**",
                    },
                    "vertical_align": "center",  # 标题区的垂直居中方式。
                    "padding": "4px 0px 4px 8px",  # 标题区的内边距。
                    "icon": {
                        # 标题前缀图标
                        "tag": "standard_icon",  # 图标类型.
                        "token": "chat-forbidden_outlined",  # 图标库中图标的 token。当 tag 为 standard_icon 时生效。
                        "color": "orange",  # 图标的颜色。当 tag 为 standard_icon 时生效。
                        "img_key": "img_v2_38811724",  # 自定义前缀图标的图片 key。当 tag 为 custom_icon 时生效。
                        "size": "16px 16px",  # 图标的尺寸。默认值为 10px 10px。
                    },
                    "icon_position": "follow_text",  # 图标的位置。默认值为 right。
                    "icon_expanded_angle": -180,  # 折叠面板展开时图标旋转的角度，正值为顺时针，负值为逆时针。默认值为 180。
                },
                "border": {
                    # 边框设置。默认不显示边框。
                    "color": "grey",  # 边框的颜色。
                    "corner_radius": "5px",  # 圆角设置。
                },
                "vertical_spacing": "8px",  # 面板内元素垂直边距设置。默认值为 8px。
                "padding": "8px 8px 8px 8px",  # 内容区的内边距。
                "elements": [
                    # 此处可添加各个组件的 JSON 结构。暂不支持表单（form）组件。
                    {
                        "tag": "markdown",
                        "content": "[1][什么是CRM系统？它的作用是什么？ - 知乎](https:#open.feishu.cn/document/server-docs/im-v1/message-reaction/emojis-introduce)\n[2][什么是 CRM？| Oracle 中国](https:#open.feishu.cn/document/server-docs/im-v1/message-reaction/emojis-introduce)\n[3][CRM系统的整体功能设计 | 人人都是产品经理](https:#open.feishu.cn/document/server-docs/im-v1/message-reaction/emojis-introduce)\n[3][高品质开源商城系统-CRMEB官网](https:#open.feishu.cn/document/server-docs/im-v1/message-reaction/emojis-introduce)",
                    }
                ],
            },
        ]
    },
    "i18n_header": {},
}


# 折线图
mock_data4 = [
    {"time": "2:00", "value": 8},
    {"time": "4:00", "value": 9},
    {"time": "6:00", "value": 11},
    {"time": "8:00", "value": 14},
    {"time": "10:00", "value": 16},
    {"time": "12:00", "value": 17},
    {"time": "14:00", "value": 17},
    {"time": "16:00", "value": 16},
    {"time": "18:00", "value": 15},
]
content4 = {
    "config": {},
    "i18n_elements": {
        "zh_cn": [
            {
                "tag": "chart",
                "chart_spec": {
                    "type": "line",
                    "title": {"text": "折线图"},
                    "data": {"values": mock_data4},  # 此处传入数据。
                    "xField": "time",
                    "yField": "value",
                },
            }
        ]
    },
    "i18n_header": {
        "zh_cn": {
            "title": {"tag": "plain_text", "content": "示例标题"},
            "subtitle": {"tag": "plain_text", "content": "示例文本111"},
            "template": "blue",
        }
    },
}

# 面积图
mock_data5 = [
    {"time": "2:00", "value": 8},
    {"time": "4:00", "value": 9},
    {"time": "6:00", "value": 11},
    {"time": "8:00", "value": 14},
    {"time": "10:00", "value": 16},
    {"time": "12:00", "value": 17},
    {"time": "14:00", "value": 17},
    {"time": "16:00", "value": 16},
    {"time": "18:00", "value": 15},
]
content5 = {
    "i18n_header": {
        "zh_cn": {
            "title": {"tag": "plain_text", "content": "示例标题"},
            "subtitle": {"tag": "plain_text", "content": "示例文本111"},
            "template": "blue",
        }
    },
    "elements": [
        {
            "tag": "chart",
            "chart_spec": {
                "type": "area",
                "title": {"text": "面积图"},
                "data": {"values": mock_data5},  # 此处传入数据。
                "xField": "time",
                "yField": "value",
            },
        }
    ],
    "header": {
        "template": "purple",
        "title": {"content": "卡片标题", "tag": "plain_text"},
    },
}

# 柱状图
mock_data6 = [
    {"type": "Autoc", "year": "1930", "value": 129},
    {"type": "Autoc", "year": "1940", "value": 133},
    {"type": "Autoc", "year": "1950", "value": 130},
    {"type": "Autoc", "year": "1960", "value": 126},
    {"type": "Autoc", "year": "1970", "value": 117},
    {"type": "Autoc", "year": "1980", "value": 114},
    {"type": "Democ", "year": "1930", "value": 22},
    {"type": "Democ", "year": "1940", "value": 13},
    {"type": "Democ", "year": "1950", "value": 25},
    {"type": "Democ", "year": "1960", "value": 29},
    {"type": "Democ", "year": "1970", "value": 38},
    {"type": "Democ", "year": "1980", "value": 41},
]
content6 = {
    "elements": [
        {
            "tag": "chart",
            "chart_spec": {
                "type": "bar",
                "title": {"text": "柱状图"},
                "data": {"values": mock_data6},  # 此处传入数据。
                "xField": ["year", "type"],
                "yField": "value",
                "seriesField": "type",
                "legends": {"visible": True, "orient": "bottom"},
            },
        }
    ],
    "header": {
        "template": "purple",
        "title": {"content": "卡片标题", "tag": "plain_text"},
    },
}

# 条形图
mock_data7 = [
    {"name": "Apple", "value": 214480},
    {"name": "Google", "value": 155506},
    {"name": "Amazon", "value": 100764},
    {"name": "Microsoft", "value": 92715},
    {"name": "Coca-Cola", "value": 66341},
    {"name": "Samsung", "value": 59890},
    {"name": "Toyota", "value": 53404},
    {"name": "Mercedes-Benz", "value": 48601},
]
content7 = {
    "elements": [
        {
            "tag": "chart",
            "chart_spec": {
                "type": "bar",
                "title": {"text": "条形图"},
                "data": {"values": mock_data7},  # 此处传入数据。
                "direction": "horizontal",
                "xField": "value",
                "yField": "name",
            },
        }
    ],
    "header": {
        "template": "purple",
        "title": {"content": "卡片标题", "tag": "plain_text"},
    },
}


test_content = {
    "config": {},
    "i18n_elements": {
        "zh_cn": [
            {
                "tag": "action",
                "actions": [
                    {
                        "tag": "button",
                        "text": {"tag": "plain_text", "content": "按钮"},
                        "type": "default",
                        "complex_interaction": True,
                        "width": "default",
                        "size": "medium",
                        "value": {"button1": "button11111111"},
                    }
                ],
            }
        ]
    },
    "i18n_header": {},
}
