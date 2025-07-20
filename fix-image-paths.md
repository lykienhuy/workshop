# Hướng dẫn sửa đường dẫn hình ảnh

## Vấn đề
Khi deploy lên GitHub Pages, hình ảnh bị mất do đường dẫn không chính xác. Trong các tệp Markdown, đường dẫn hình ảnh đang được viết là `/images/...` nhưng baseURL của trang web là `https://lykienhuy.github.io/workshop/`.

## Giải pháp
Có hai cách để sửa vấn đề này:

### Cách 1: Sửa đường dẫn trong các tệp Markdown
Thay đổi tất cả đường dẫn hình ảnh từ:
```
![VPC](/images/2.prerequisite/Chuanbi-(1).png)
```
thành:
```
![VPC](../../../images/2.prerequisite/Chuanbi-(1).png)
```
hoặc:
```
![VPC]({{< baseurl >}}/images/2.prerequisite/Chuanbi-(1).png)
```

### Cách 2: Sử dụng shortcode Hugo
Tạo một shortcode mới trong thư mục `layouts/shortcodes/img.html` với nội dung:
```html
{{ $src := .Get "src" }}
<img src="{{ .Site.BaseURL }}{{ $src }}" alt="{{ .Get "alt" }}" />
```

Sau đó sử dụng shortcode này trong các tệp Markdown:
```
{{< img src="/images/2.prerequisite/Chuanbi-(1).png" alt="VPC" >}}
```

## Cấu hình đã thực hiện
Đã thêm các cấu hình sau vào `config.toml`:
- `relativeURLs = true`: Đảm bảo các URL trong trang web là tương đối
- `uglyURLs = false`: Giữ cấu trúc URL đẹp
- Đã vô hiệu hóa cấu hình cache hình ảnh có thể gây vấn đề

## Kiểm tra sau khi sửa
Sau khi thực hiện các thay đổi, hãy build lại trang web và kiểm tra xem hình ảnh đã hiển thị đúng chưa:
```
hugo server -D
```