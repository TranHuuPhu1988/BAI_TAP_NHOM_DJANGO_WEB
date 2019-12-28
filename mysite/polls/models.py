from django.db import models

class NhaCungCap(models.Model):
    MaNhaCungCap = models.CharField(max_length=200, primary_key=True)
    TenNhaCungCap = models.CharField(max_length=200)
    DiaChi = models.CharField(max_length=200)
    SoDienThoai = models.CharField(max_length=200)
    LoGo = models.CharField(max_length=200)

class LoaiSanPham(models.Model):
    MaNhaCungCap = models.CharField(max_length=200)
    MaLoai = models.CharField(max_length=200, primary_key=True)
    TenLoai = models.CharField(max_length=200)
    MoTa = models.CharField(max_length=200)

class TaiKhoang(models.Model):
    TenTaiKhoang = models.CharField(max_length=200 , primary_key=True)
    MatKhau = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)


class SanPham(models.Model):
    MaSanPham = models.CharField(max_length=200, primary_key=True)
    Ten = models.CharField(max_length=200)
    GiaDaGiam = models.IntegerField(default=0)
    GiaBan = models.IntegerField(default=0)
    Soluong = models.IntegerField(default=0)
    NhaCungCap = models.CharField(max_length=200)
    MaLoai = models.CharField(max_length=200)
    HinhAnh = models.CharField(max_length=200)
    SoluongNhap = models.CharField(max_length=200)

class ThongTinSanPham(models.Model):
    MaSanPham = models.CharField(max_length=200 , primary_key=True)
    MoTa = models.CharField(max_length=200)
    HinhAnhChiTiet = models.CharField(max_length=200)
    
class DonHang(models.Model):
    MaDonHang = models.CharField(max_length=200,primary_key=True)
    TenKhachHang = models.CharField(max_length=200)
    DanhSachMaSanPham = models.CharField(max_length=200)
    DanhSachTenSanPham = models.CharField(max_length=200)
    TongSoLuong = models.IntegerField(default=0)
    TongTien = models.IntegerField(default=0)
    NgayMua = models.DateTimeField('date published')
    DiaChi = models.CharField(max_length=200)
    Email= models.CharField(max_length=200)
    TinhTrangDonHang = models.CharField(max_length=200)

class Order(models.Model):
    MaOrder = models.CharField(max_length=200,primary_key=True)
    Images = models.CharField(max_length=200)
    GiaDaGiam = models.IntegerField(default=0)
    TenSanPham = models.CharField(max_length=200)