from datetime import date

class Employee:
    def __init__(self, full_name, birth_date, hire_date):
        self.full_name = full_name
        self.birth_date = birth_date
        self.hire_date = hire_date

    def get_age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age

    def get_years_of_service(self):
        today = date.today()
        years_of_service = today.year - self.hire_date.year
        if (today.month, today.day) < (self.hire_date.month, self.hire_date.day):
            years_of_service -= 1
        return years_of_service


# Sử dụng lớp Employee để quản lý nhân viên trong công ty
# Tạo các đối tượng nhân viên mới
employee1 = Employee("Trần Văn A", date(2000, 5, 16), date(2023, 14 ,4))
employee2 = Employee("Trần Văn D", date(1991, 11 ,13), date(2020 ,23 ,5))

# In thông tin của từng nhân viên và tuổi/tổng số năm làm việc của họ.
print(f"Nhân viên: {employee1.full_name}")
print(f"Ngày sinh: {employee1.birth_date}")
print(f"Tuổi: {employee1.get_age()}")
print(f"Ngày vào công ty: {employee1.hire_date}")
print(f"Tổng số năm làm việc: {employee1.get_years_of_service()}")

print("\n")

print(f"Nhân viên: {employee2.full_name}")
print(f"Ngày sinh: {employee2.birth_date}")
print(f"Tuổi: {employee2.get_age()}")
print(f"Ngày vào công ty: {employee2.hire_date}")
print(f"Tổng số năm làm việc: {employee2.get_years_of_service()}")
