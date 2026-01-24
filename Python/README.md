# Nhật ký học Python tuần 1 (19-25/01/2026)

### 1. Kiểu dữ liệu, nhập và in

- Kiểu dữ liệu không cần khai báo mà được định nghĩa theo giá trị của biến

**Ví dụ:**
```
a = 1 // kiểu nguyên
b = 3.14 // kiểu thực
c = "Hello PTIT" // kiểu ký tự
d = 'Hello PTIT'
e = '''Hello PTIT'''
f = '''hello PTIT'''''
g = True // kiểu bool, true/false
h = 1j // kiểu số phức
```

- In ra màn: *mặc định in sẽ xuống dòng*
    
    print("Chuỗi cần in", <biến cần in>) 

    a = "hello"

    b = "ptit"

    print(a + " " + b) // -> hello ptit. ***Ghép chuỗi***

- Nhập vào biến:
    
    <tên biến> = input() // mặc định là dạng string
    
    <tên biến> = KDL(input()) // ép kiểu cho biến được nhập vào

**Ví dụ:** 

```
b = 6
print("Gia tri cua b la", b)
a = int(input()) // nhập vào biến a 1 số kiểu nguyên
```

### 2. Cấu trúc dữ liệu

**- Cấu trúc dữ liệu danh sách (list):** tập hợp có thứ tự và có thể thay đổi. Các phần tử trong danh sách được đặt trong dấu ngoặc vuông ([]), và được phân tách bởi dấu phẩy. Ví dụ:

```
a = [1, 2, 3, 4, 5]
```

**- Cấu trúc dữ liệu bộ (tuple):** Kiểu tuple tương tự như kiểu danh sách, nhưng không thể thay đổi (nghĩa là bạn không thể thêm, xóa hoặc sửa đổi các phần tử trong bộ). Các phần tử trong bộ được đặt trong dấu ngoặc đơn (()), và được phân tách bởi dấu phẩy. Ví dụ:

```
b = (1, 2, 3, 4, 5)
```

**- Cấu trúc dữ liệu tập hợp (set):** Kiểu set là một tập hợp không có thứ tự và không chứa các phần tử trùng lặp. Các phần tử trong tập hợp được đặt trong dấu ngoặc nhọn ({}), và được phân tách bởi dấu phẩy. Ví dụ:

```
c = {1, 2, 3, 4, 5}
```

**- Cấu trúc dữ liệu từ điển (dictionary):** Kiểu dictionary là một tập hợp không có thứ tự, có thể thay đổi và có các phần tử được xác định bởi một khóa duy nhất. Các phần tử trong từ điển được đặt trong dấu ngoặc nhọn ({}), và mỗi phần tử bao gồm một cặp khóa-giá trị. Ví dụ:

```
d = {"name": "John", "age": 30}
```
