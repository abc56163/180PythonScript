menus={
    "安徽":{
        "合肥":{
            "蜀山区":{
                "学校":["三十六中","五十四中"],
                "旅馆":["速八","假日"]
    }
        }
    },
    "北京":{
        "昌平":{
            "学校":["清华大学","北大"],
            "旅馆":["桔子水晶","七天"]
                }
            }

    }

exit = False
while not exit:
    print("*"*20)
    for i in menus:
        print(i,menus[i])
    print("*"*20)
    put = input("input city:")
    while not exit:
        for i2 in menus[put]:
            print(i2)


