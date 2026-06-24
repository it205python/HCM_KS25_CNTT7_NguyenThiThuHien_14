class RestaurantBill:
    def __init__(self, id, customer_name, table_number, food_amount, vat_rate, service_fee, discount):
        self.id = id
        self.customer_name = customer_name
        self.table_number = table_number
        self.food_amount = food_amount
        self.vat_rate = vat_rate
        self.service_fee = service_fee
        self.discount = discount
        self.total_bill = 0
        self.bill_type = ""

    def calculate_total_bill(self):
        self.total_bill = self.food_amount + self.vat_rate + self.service_fee - self.discount

    def classify_bill(self):
        if self.total_bill >= 5000000:
            self.bill_type = "VIP"
        elif self.total_bill >= 2000000:
            self.bill_type = "Lớn"
        elif self.total_bill >= 500000:
            self.bill_type = "Trung bình"
        elif self.total_bill < 500000 and self.total_bill >= 0:
            self.bill_type = "Nhỏ"

class RestaurantBillManager():
    def __init__(self):
        self.bills: list[RestaurantBill] = []

    def add_bill(self):
        found = False
        print("\n=== THÊM HÓA ĐƠN MỚI ===")
        id = input("Nhập mã hóa đơn: ").strip().upper()
        if not id:
            print("Mã hóa đơn không được để trống")
            return

        for item in self.bills:
            if id == item.id:
                found = True

        if found == True:
            print("Mã hóa đơn đã tồn tại")
            return
        
        while True:
            customer_name = input("Nhập tên khách hàng: ").strip()
            if not customer_name:
                print("Tên khách hàng không được để trống")
                continue
            break

        while True:
            try:
                table_number = int(input("Nhập số bàn: "))
                if not table_number:
                    continue
                if table_number <= 0:
                    print("Số bàn ăn phải lớn hơn 0")
                    continue
                break
            except:
                print("Số bàn ăn không hợp lệ")

        while True:
            try:
                food_amount = int(input("Nhập tiền món ăn: "))
                if food_amount < 0:
                    print("Tiền món ăn phải lớn hơn hoặc bằng 0")
                    continue
                break
            except:
                print("Tiền món ăn phải lớn hơn hoặc bằng 0")

        while True:
            try:
                vat_rate = float(input("Nhập tỷ lệ VAT: "))
                if (vat_rate < 0 or vat_rate > 100):
                    print("Tỷ lệ VAT phải là số từ 0 đến 100")
                    continue
                break
            except:
                print("Tỷ lệ VAT phải là số từ 0 đến 100")

        while True:
            try:
                service_fee = int(input("Nhập phí dịch vụ: "))
                if service_fee < 0:
                    print("Phí dịch vụ phải lớn hơn hoặc bằng 0")
                    continue
                break
            except:
                print("Phí dịch vụ phải lớn hơn hoặc bằng 0")

        while True:
            try:
                discount = float(input("Nhập giảm giá: "))
                if discount < 0:
                    print("Giảm giá phải lớn hơn hoặc bằng 0")
                    continue
                break
            except:
                print("Giảm giá phải lớn hơn hoặc bằng 0")

        new_bill = RestaurantBill(id, customer_name, table_number, food_amount, vat_rate, service_fee, discount)
        new_bill.calculate_total_bill()
        new_bill.classify_bill()
        self.bills.append(new_bill)
        print("Thêm hóa đơn bàn ăn thành công!")

    def show_all(self):
        if len(self.bills) == 0:
            print("Danh sách hóa đơn bàn ăn đang rỗng!")
            return
        
        print("\n=== DANH SÁCH HÓA ĐƠN ===")
        print(
            f"{'Mã hóa đơn':10} | "
            f"{'Tên khách hàng':20} | "
            f"{'Số bàn':10} | "
            f"{'Tiền món ăn':15} | "
            f"{'Tỷ lệ VAT':10} | "
            f"{'Phí dịch vụ':15} | "
            f"{'Giảm giá':15} | "
            f"{'Tổng tiền hóa đơn':20} | "
            f"{'Phân loại hóa đơn'}")
        for item in self.bills:
            print(
                f"{item.id:<10} | "
                f"{item.customer_name:<20} | "
                f"{item.table_number:<10} | "
                f"{item.food_amount:<15} | "
                f"{item.vat_rate:<10} | "
                f"{item.service_fee:<15} | "
                f"{item.discount:<15} | "
                f"{item.total_bill:<20} | "
                f"{item.bill_type}")

    def update_bill(self):
        if len(self.bills) == 0:
            print("Danh sách hóa đơn bàn ăn đang rỗng!")
            return
        
        found = False
        print("\n=== CẬP NHẬT HÓA ĐƠN ===")
        id = input("Nhập mã hóa đơn cần cập nhật: ").strip().upper()
        if not id:
            print("Mã hóa đơn không được để trống")
            return

        for item in self.bills:
            if id == item.id:
                found = True
                while True:
                    try:
                        food_amount_new = int(input("Nhập tiền món ăn mới: "))
                        if food_amount_new < 0:
                            print("Tiền món ăn phải lớn hơn hoặc bằng 0")
                            continue
                        break
                    except:
                        print("Tiền món ăn phải lớn hơn hoặc bằng 0")

                while True:
                    try:
                        vat_rate_new = float(input("Nhập tỷ lệ VAT mới: "))
                        if (vat_rate_new < 0 or vat_rate_new > 100):
                            print("Tỷ lệ VAT phải là số từ 0 đến 100")
                            continue
                        break
                    except:
                        print("Tỷ lệ VAT phải là số từ 0 đến 100")

                while True:
                    try:
                        service_fee_new = int(input("Nhập phí dịch vụ mới: "))
                        if service_fee_new < 0:
                            print("Phí dịch vụ phải lớn hơn hoặc bằng 0")
                            continue
                        break
                    except:
                        print("Phí dịch vụ phải lớn hơn hoặc bằng 0")

                while True:
                    try:
                        discount_new = float(input("Nhập giảm giá mới: "))
                        if discount_new < 0:
                            print("Giảm giá phải lớn hơn hoặc bằng 0")
                            continue
                        break
                    except:
                        print("Giảm giá phải lớn hơn hoặc bằng 0")

                item.food_amount = food_amount_new
                item.vat_rate = vat_rate_new
                item.service_fee = service_fee_new
                item.discount = discount_new
                item.calculate_total_bill()
                item.classify_bill()
                print("Cập nhật hóa đơn thành công!")

        if found == False:
            print("Không tìm thấy hóa đơn cần cập nhật")
            return

    def delete_bill(self):
        found = False
        if len(self.bills) == 0:
            print("Danh sách hóa đơn bàn ăn đang rỗng!")
            return

        print("\n=== XÓA HÓA ĐƠN ===")
        id = input("Nhập mã hóa đơn cần xóa: ").strip().upper()
        if not id:
            print("Mã hóa đơn không được để trống")
            return

        for item in self.bills:
            if id == item.id:
                found = True
                while True:
                    confirm = input("Bạn có chắc muốn xóa hóa đơn này không? (Y/N): ").lower()
                    if confirm == "y":
                        self.bills.remove(item)
                        print("Đã xóa hóa đơn thành công")
                        return
                    elif confirm == "n":
                        print("Đã hủy thao tác")
                        return
                    else:
                        print("Vui lòng chọn Y hoặc N")

        if found == False:
            print("Không tìm thấy hóa đơn cần xóa!")
            return

    def search_bill(self):
        found = False
        if len(self.bills) == 0:
            print("Danh sách hóa đơn bàn ăn đang rỗng!")
            return

        print("\n=== TÌM KIẾM HÓA ĐƠN ===")
        while True:
            search = input("""\n1. Tìm theo tên khách hàng
2. Tìm theo số bàn
3. Thoát
Nhập lựa chọn của bạn: """)
            match search:
                case "1":
                    found = False
                    search_customer_name = input(
                        "Nhập tên khách hàng cần tìm: ").strip().lower()
                    if not search_customer_name:
                        print("Tên khách hàng hoặc số bàn không được để trống")
                        return
                    print(
                        f"{'Mã hóa đơn':10} | "
                        f"{'Tên khách hàng':20} | "
                        f"{'Số bàn':10} | "
                        f"{'Tiền món ăn':15} | "
                        f"{'Tỷ lệ VAT':10} | "
                        f"{'Phí dịch vụ':15} | "
                        f"{'Giảm giá':15} | "
                        f"{'Tổng tiền hóa đơn':20} | "
                        f"{'Phân loại hóa đơn'}")
                    for item in self.bills:
                        if search_customer_name in item.customer_name.lower():
                            found = True
                            print(
                                f"{item.id:<10} | "
                                f"{item.customer_name:<20} | "
                                f"{item.table_number:<10} | "
                                f"{item.food_amount:<15} | "
                                f"{item.vat_rate:<10} | "
                                f"{item.service_fee:<15} | "
                                f"{item.discount:<15} | "
                                f"{item.total_bill:<20} | "
                                f"{item.bill_type}")
                    if found == False:
                        print("Không tìm thấy hóa đơn phù hợp!")
                        return
                case "2":
                    found = False
                    search_table_number = int(input("Nhập số bàn cần tìm: "))
                    if not search_table_number:
                        print("Tên khách hàng hoặc số bàn không được để trống")
                        return
                    print(
                        f"{'Mã hóa đơn':10} | "
                        f"{'Tên khách hàng':20} | "
                        f"{'Số bàn':10} | "
                        f"{'Tiền món ăn':15} | "
                        f"{'Tỷ lệ VAT':10} | "
                        f"{'Phí dịch vụ':15} | "
                        f"{'Giảm giá':15} | "
                        f"{'Tổng tiền hóa đơn':20} | "
                        f"{'Phân loại hóa đơn'}")
                    for item in self.bills:
                        if search_table_number in item.table_number:
                            found = True
                            print(
                                f"{item.id:<10} | "
                                f"{item.customer_name:<20} | "
                                f"{item.table_number:<10} | "
                                f"{item.food_amount:<15} | "
                                f"{item.vat_rate:<10} | "
                                f"{item.service_fee:<15} | "
                                f"{item.discount:<15} | "
                                f"{item.total_bill:<20} | "
                                f"{item.bill_type}")
                    if found == False:
                        print("Không tìm thấy hóa đơn phù hợp!")
                        return
                case "3":
                    print("Thoát chương trình tìm kiếm")
                    break
                case _:
                    print("Lựa chọn không hợp lệ vui lòng chọn (1-3)")

def menu():
    print("""\n======= MENU =======
1. Hiển thị danh sách hóa đơn
2. Thêm hóa đơn mới
3. Cập nhật hóa đơn
4. Xóa hóa đơn
5. Tìm kiếm hóa đơn
6. Thoát
=================================""")

def main():
    restaurant_bill_manager = RestaurantBillManager()
    while True:
        menu()
        user_choice = input("Nhập lựa chọn của bạn: ")
        match user_choice:
            case "1":
                restaurant_bill_manager.show_all()
            case "2":
                restaurant_bill_manager.add_bill()
            case "3":
                restaurant_bill_manager.update_bill()
            case "4":
                restaurant_bill_manager.delete_bill()
            case "5":
                restaurant_bill_manager.search_bill()
            case "6":
                print("Cảm ơn bạn đã sử dụng hệ thống quản lý nhà hàng!")
                break
            case _:
                print("Lựa chọn không hợp lệ, vui lòng chọn lại (1-6)")

if __name__ == "__main__":
    main()