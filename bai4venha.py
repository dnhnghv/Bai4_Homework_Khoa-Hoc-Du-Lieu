import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu
tep_du_lieu = "weather_data_filtered.csv"  # Đổi tên file nếu cần

# Đọc dữ liệu với hàng đầu tiên làm tiêu đề
du_lieu = pd.read_csv(tep_du_lieu, header=0)
print("Danh sách cột:", du_lieu.columns)

# Chọn thành phố để phân tích
thanh_pho = "New York"
if thanh_pho not in du_lieu.columns:
    raise KeyError(f"Cột '{thanh_pho}' không tồn tại trong dữ liệu. Hãy chọn một thành phố hợp lệ!")

# Chuyển cột thời gian về dạng datetime
du_lieu["datetime"] = pd.to_datetime(du_lieu["datetime"])

# Trích xuất thông tin thời gian
du_lieu["nam"] = du_lieu["datetime"].dt.year
du_lieu["thang"] = du_lieu["datetime"].dt.month
du_lieu["ngay_trong_tuan"] = du_lieu["datetime"].dt.dayofweek
du_lieu["gio"] = du_lieu["datetime"].dt.hour

# Lấy mẫu lại dữ liệu theo ngày
nhiet_do_hang_ngay = du_lieu.resample("D", on="datetime")[thanh_pho].mean().reset_index()

# Nội suy dữ liệu bị thiếu
nhiet_do_hang_ngay[thanh_pho] = nhiet_do_hang_ngay[thanh_pho].interpolate()

# Tính toán xu hướng nhiệt độ trung bình theo tháng
nhiet_do_trung_binh_thang = du_lieu.groupby(["nam", "thang"])[thanh_pho].mean().reset_index()

# Vẽ biểu đồ
plt.figure(figsize=(10, 5))
plt.plot(nhiet_do_trung_binh_thang["thang"], nhiet_do_trung_binh_thang[thanh_pho], marker='o', linestyle='-')
plt.xlabel("Tháng")
plt.ylabel("Nhiệt độ trung bình (°C)")
plt.title(f"Xu hướng nhiệt độ trung bình theo tháng tại {thanh_pho}")
plt.grid()
plt.show()
