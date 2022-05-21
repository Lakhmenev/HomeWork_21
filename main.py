from classes import Store, Shop, Request


def main():
    print('Строим склад на 150 мест хранения')
    store = Store(None, 150)
    print('Загружаем склад')
    store.add('печеньки', 10)
    store.add('фрукты', 20)
    store.add('консервы', 50)
    store.add('печеньки', 20)
    print('На складе в наличии:')
    temp_dict = store.get_items()
    for key, value in temp_dict.items():
        print(f'{value} позиций - "{key}"')
    print(f'Количество уникальных позиций {store.get_unique_items_count()}')
    print("Свободного места на складе осталось", store.get_free_space())
    print()
    print('Открываем магазин на 25 позиций')
    shop = Shop(None, 25, 5)
    print()

    input_user = input('Введите строку типа: "Доставить 3 печеньки из склад в магазин" \n')

    data_req = Request(input_user)
    result_store = store.remove(data_req.product_name, data_req.amount)
    if result_store[0]:
        print(f'Курьер забрал {result_store[2]} {result_store[1]}')
        print(f'Курьер везет {result_store[2]} {result_store[1]} со склад в магазин')
        result_shop = shop.add(result_store[1], result_store[2])
        #  Возврат товара назад на склад если его не принял магазин
        if not result_shop[0]:
            store.add(result_shop[1], result_shop[2])
            print(f'Товар {result_shop[1]} в кол-ве {result_shop[2]} был возвращён на склад')
        else:
            print(f'Курьер доставил {result_store[2]} {result_store[1]} со склад в магазин')

    print()
    print('На складе в наличии:')
    temp_dict = store.get_items()
    for key, value in temp_dict.items():
        print(f'{value} позиций - "{key}"')
    print()
    print('В магазине сейчас в наличии:')
    temp_dict = shop.get_items()
    for key, value in temp_dict.items():
        print(f'{value} позиций - "{key}"')



if __name__ == '__main__':
    main()
