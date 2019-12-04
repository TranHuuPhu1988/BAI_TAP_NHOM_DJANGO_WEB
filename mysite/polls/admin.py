from django.contrib import admin

from .models import LoaiSanPham
from .models import TaiKhoang
from .models import NhaCungCap
from .models import ThongTinSanPham
from .models import DonHang
from .models import SanPham

admin.site.register(LoaiSanPham)
admin.site.register(TaiKhoang)
admin.site.register(NhaCungCap)
admin.site.register(ThongTinSanPham)
admin.site.register(DonHang)
admin.site.register(SanPham)