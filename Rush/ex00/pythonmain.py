from typing import List, Dict
from datetime import datetime

class LibraryBooking:
    def __init__(self, user_name: str, book_title: str, room_type: str, date: str, duration: int):
        self.user_name = user_name
        self.book_title = book_title
        self.room_type = room_type  # ห้องเดี่ยว/ห้องกลุ่ม/พื้นที่อ่านหนังสือ
        self.date = date
        self.duration = duration  # ชั่วโมง

class BookingManager:
    def __init__(self):
        self.bookings: List[LibraryBooking] = []
    
    def add_booking(self, user_name: str, book_title: str, room_type: str, date: str, duration: int):
        """เพิ่มการจองใหม่"""
        new_booking = LibraryBooking(user_name, book_title, room_type, date, duration)
        self.bookings.append(new_booking)
        print(f"จอง {room_type} สำหรับ {book_title} สำเร็จ!")
    
    def show_all_bookings(self):
        """แสดงการจองทั้งหมด"""
        if not self.bookings:
            print("ยังไม่มีรายการจอง")
            return
        
        print("\n=== รายการจองทั้งหมด ===")
        for i, booking in enumerate(self.bookings, 1):
            print(f"{i}. {booking.user_name} จอง {booking.room_type}")
            print(f"   หนังสือ: {booking.book_title}")
            print(f"   วันที่: {booking.date} เป็นเวลา {booking.duration} ชั่วโมง\n")
    
    def cancel_booking(self, booking_index: int):
        """ยกเลิกการจอง"""
        if 1 <= booking_index <= len(self.bookings):
            canceled = self.bookings.pop(booking_index - 1)
            print(f"ยกเลิกการจอง {canceled.book_title} ของ {canceled.user_name} แล้ว")
        else:
            print("ไม่พบรายการจองนี้")
    
    def available_rooms(self):
        """แสดงห้องที่ว่าง"""
        room_types = ["ห้องเดี่ยว", "ห้องกลุ่ม", "พื้นที่อ่านหนังสือ"]
        print("\n=== ห้องที่ว่างในวันนี้ ===")
        for room in room_types:
            count = sum(1 for b in self.bookings if b.room_type == room and b.date == datetime.now().strftime("%d/%m/%Y"))
            print(f"{room}: {10 - count} จาก 10 ห้องว่าง")

def display_menu():
    """แสดงเมนูหลัก"""
    print("\n" + "="*50)
    print("ระบบจองห้องสมุด (Library Booking System)")
    print("="*50)
    print("1. จองหนังสือ/ห้องศึกษา")
    print("2. แสดงการจองทั้งหมด")
    print("3. ยกเลิกการจอง")
    print("4. ตรวจสอบห้องว่าง")
    print("5. ออกจากระบบ")
    print("="*50)

def main():
    manager = BookingManager()
    
    while True:
        display_menu()
        choice = input("เลือกเมนู (1-5): ").strip()
        
        if choice == "1":
            name = input("ชื่อผู้จอง: ")
            book = input("ชื่อหนังสือที่ต้องการ: ")
            room = input("ประเภทห้อง (ห้องเดี่ยว/ห้องกลุ่ม/พื้นที่อ่านหนังสือ): ")
            date = input("วันที่จอง (dd/mm/yyyy): ")
            hours = int(input("จำนวนชั่วโมง: "))
            manager.add_booking(name, book, room, date, hours)
        
        elif choice == "2":
            manager.show_all_bookings()
        
        elif choice == "3":
            manager.show_all_bookings()
            if manager.bookings:
                try:
                    num = int(input("เลือกลำดับการจองที่ต้องการยกเลิก: "))
                    manager.cancel_booking(num)
                except ValueError:
                    print("กรุณากรอกตัวเลขเท่านั้น")
        
        elif choice == "4":
            manager.available_rooms()
        
        elif choice == "5":
            print("\nขอบคุณที่ใช้บริการห้องสมุดของเรา!")
            break
        
        else:
            print("กรุณาเลือกเมนู 1-5 เท่านั้น")

if __name__ == "__main__":
    main()
