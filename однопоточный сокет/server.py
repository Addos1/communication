# Импорт модуля сокета
import socket

# Здесь мы используем IP-адрес локального хоста
# и номер порта
LOCALHOST = "127.0.0.1"
PORT = 8080
# вызов метода сокета сервера
server = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))
server.listen(1)
print("Сервер запущен")
print("Ожидание запроса клиента...")
# Здесь серверный сокет готов для
# получения ввода от пользователя
clientConnection, clientAddress = server.accept()
print("Подключенный клиент:", clientAddress)
msg = ''
# Запуск бесконечного цикла
while True:
    data = clientConnection.recv(1024)
    msg = data.decode()
    if msg == 'Конец':
        print("Соединение завершено")
        break

    print("Уравнение получено")
    result = 0
    operation_list = msg.split()
    oprnd1 = operation_list[0]
    operation = operation_list[1]
    oprnd2 = operation_list[2]
    # здесь мы меняем str на float
    num1 = float(oprnd1)
    num2 = float(oprnd2)
    # Здесь мы выполняем базовую арифметическую операцию

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2

    elif operation == "/":
        try:
            result = num1 / num2
        except ZeroDivisionError:
            result = "На 0 делить нельзя"

    elif operation == "*":
        result = num1 * num2

    else:
        print ("на 0 делить нельзя")

    print("Отправить результат клиенту")
    # Здесь мы меняем float на string и
    # после кодирования отправить вывод клиенту
    output = str(result)

    clientConnection.send(output.encode())
clientConnection.close()