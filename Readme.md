- print : Hàm in chuỗi ký tữ ra màn hình.
- Biến: <tên biến> = <Giá trị của biến>
    + Biến trong python sẽ tự động khởi tạo kiểu dữ liệu cho biến.
    + Dung hàm type() để kiểm tra kiêu dư liệu của biến.
    + Kiểu số nguyên trong python được hỗ trợ vô hạn.
    + Muốn giới hạn chữ số của một số ta sử dụng kiểu dữ liệu decimal.
        /Cú pháp:   getcontext().prec = <tổng số lượng chữ số>
                    d = Decimal(...) / Decimal(...)
    + Kiểu dữ liệu thập phân.
        Cú pháp:   f = Fraction(<tử số>, <mẫu số>)
    + Số phức:  c = complex(<phần thực>, <phần ảo>)
                c.real: lấy phần thực.
                c.imag: lấy phần ảo.
- Biểu thức toán học trong python:
    + X + Y: Tổng X và Y.
    + X - Y: Hiệu X và Y.
    + X * Y: Tích X và Y.
    + X / Y: Thương X và Y, kết quả luôn là một số thực.
    + X // Y: Phép chia lấy phần nguyên.
    + X % Y: Phép chia lấy phần dư.
    + X ** Y: Luỹ thừa X cơ số Y.