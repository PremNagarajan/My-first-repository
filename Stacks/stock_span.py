def find_stock_span(price):
    stack = list()
    result = [1] * len(price)
    stack.append(0)

    for i in range(1, len(price)):
        curr = price[i]
        while stack and curr > price[stack[-1]]:
            stack.pop()

        if not stack:
            result[i] = i+1
        else:
            result[i] = i-stack[-1]

        stack.append(i)
    return result

price = [10, 4, 5, 90, 120, 80]
print price
result = find_stock_span(price)
print result