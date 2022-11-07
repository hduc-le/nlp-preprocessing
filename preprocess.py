import re

def remove_newlines_tabs(text):
    """
    This function will remove all the occurrences of newlines, tabs, and combinations like: \\n, \\.
    
    arguments:
        input_text: "text" of type "String". 
                    
    return:
        value: "text" after removal of newlines, tabs, \\n, \\ characters.
        
    Example:
    Input : This is her \\ first day at this place.\n Please,\t Be nice to her.\\n
    Output : This is her first day at this place. Please, Be nice to her. 
    
    """
    
    # Replacing all the occurrences of \n,\\n,\t,\\ with a space.
    Formatted_text = text.replace('\\n', ' ').replace('\n', ' ').replace('\t',' ').replace('\\', ' ').replace('. com', '.com')
    return Formatted_text


def remove_links(text):
    """
    This function will remove all the occurrences of links.
    
    arguments:
        input_text: "text" of type "String". 
                    
    return:
        value: "text" after removal of all types of links.
        
    Example:
    Input : To know more about this website: kajalyadav.com  visit: https://kajalyadav.com//Blogs
    Output : To know more about this website: visit:     
    
    """
    
    # Removing all the occurrences of links that starts with https
    remove_https = re.sub(r'http\S+', '', text)
    # Remove all the occurrences of text that ends with .com
    remove_com = re.sub(r"\ [A-Za-z]*\.com", " ", remove_https)
    return remove_com

def remove_whitespace(text):
    """ This function will remove 
        extra whitespaces from the text
    arguments:
        input_text: "text" of type "String". 
                    
    return:
        value: "text" after extra whitespaces removed .
        
    Example:
    Input : How   are   you   doing   ?
    Output : How are you doing ?     
        
    """
    return ' '.join(text.split())

def lower_casing_text(text):
    
    """
    The function will convert text into lower case.
    
    arguments:
         input_text: "text" of type "String".
         
    return:
         value: text in lowercase
         
    Example:
    Input : The World is Full of Surprises!
    Output : the world is full of surprises!
    
    """
    # Convert text to lower case
    # lower() - It converts all upperase letter of given string to lowercase.
    text = text.lower()
    return text

def removing_special_characters(text):
    """Removing all the special characters except the one that is passed within 
       the regex to match, as they have imp meaning in the text provided.
   
    
    arguments:
         input_text: "text" of type "String".
         
    return:
        value: Text with removed special characters that don't require.
        
    Example: 
    Input : Hello, K-a-j-a-l. Thi*s is $100.05 : the payment that you will recieve! (Is this okay?) 
    Output :  Hello, Kajal. This is $100.05 : the payment that you will recieve! Is this okay?
    
   """
    # The formatted text after removing not necessary punctuations.
    Formatted_Text = re.sub(r"[^a-z0-9A-Z_ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂưăạảấầẩẫậắằẳẵặẹẻẽềềểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳỵỷỹ]+", ' ', text) 
    # Formatted_Text = re.sub("\W+",' ', text)
    # In the above regex expression,I am providing necessary set of punctuations that are frequent in this particular dataset.
    return Formatted_Text

def removing_numbers(text):
    """Removing all numbers.
   
    
    arguments:
         input_text: "text" of type "String".
         
    return:
        value: Text with removed numbers that don't require.
        
    Example: 
    Input : Hello, Kajal. This is $. : the payment that you will recieve! (Is this okay?) 
    Output :  Hello, Kajal. This is $100.05 : the payment that you will recieve! Is this okay?
    
   """
    # The formatted text after removing numbers.
    Formatted_Text = re.sub("^\d+\s|\s\d+\s|\s\d+$", " ", text)
    # Formatted_Text = re.sub("\W+",' ', text)
    return Formatted_Text


def main():
    TXT = """Hà Giang

Hà Giang là một tỉnh thuộc vùng Đông Bắc Bộ, Việt Nam.

Năm 2018, Hà Giang là đơn vị hành chính Việt Nam đông thứ 48 về số dân, xếp thứ 58 về Tổng sản phẩm trên địa bàn (GRDP) và là tỉnh nghèo trong số 6 tỉnh nghèo nhất cả nước, có huyện Xín Mần thuộc diện huyện nghèo trong 6 huyện nghèo nhất cả nước, xếp thứ 63 về GRDP bình quân đầu người, đứng thứ 58 về tốc độ tăng trưởng GRDP. Với 846.500 người dân, GRDP đạt 20.772 tỉ Đồng (tương ứng với 0,7610 tỉ USD), GRDP bình quân đầu người đạt 20,7 triệu đồng (tương ứng với 899 USD), tốc độ tăng trưởng GRDP đạt 6,76%.

== Địa lý. ==
=== Vị trí địa lí. ===
Tỉnh Hà Giang nằm ở cực bắc Việt Nam, có vị trí địa lý:
BULLET::::- Phía đông giáp tỉnh Cao Bằng
BULLET::::- Phía tây giáp các tỉnh Yên Bái và Lào Cai
BULLET::::- Phía nam giáp tỉnh Tuyên Quang
BULLET::::- Phía bắc giáp châu tự trị dân tộc Choang và Miêu Văn Sơn thuộc tỉnh Vân Nam và địa cấp thị Bách Sắc thuộc khu tự trị dân tộc Choang Quảng Tây, Cộng hòa Nhân dân Trung Hoa .

==== Các điểm cực của tỉnh Hà Giang:. ====
BULLET::::- Điểm cực bắc tại: xã Lũng Cú, huyện Đồng Văn.
BULLET::::- Điểm cực đông tại: bản Lủng Chỉn, xã Sơn Vĩ, huyện Mèo Vạc.
BULLET::::- Điểm cực tây tại: bản Ma Li Sán, xã Pà Vầy Sủ, huyện Xín Mần.
BULLET::::- Điểm cực nam tại: xã Đồng Yên, huyện Bắc Quang.

Trung tâm hành chính của tỉnh là Thành phố Hà Giang, cách Thủ đô Hà Nội 320 km. Địa hình của tỉnh Hà Giang khá phức tạp, có nhiều ngọn núi đá cao và sông suối , có thể chia làm 3 vùng. Vùng cao núi đá phía bắc nằm sát chí tuyến bắc, có độ dốc khá lớn, thung lũng và sông suối bị chia cắt nhiều. Nằm trong vùng khí hậu cận nhiệt đới ẩm nhưng do địa hình cao nên khí hậu Hà Giang mang nhiều sắc thái ôn đới. Vùng cao núi đất phía tây thuộc khối núi thượng nguồn sông Chảy, sườn núi dốc, đèo cao, thung lũng và lòng suối hẹp.Vùng thấp trong tỉnh gồm vùng đồi núi, thung lũng sông Lô và Thành phố Hà Giang.

Hà Giang có nhiều núi non hùng vĩ, ngoài hai đỉnh núi cao là Tây Côn Lĩnh (2419 m) và Chiêu Lầu Thi (2402m), ở đây còn có các cao nguyên đá tai mèo lởm chởm đặc trưng với những vách đá dựng đứng. Về thực vật, Hà Giang có nhiều khu rừng nguyên sinh, nhiều gỗ quý, và có tới 1000 loại cây dược liệu. Động vật có hổ, chim công, chim trĩ, tê tê, và nhiều loài khác.

=== Khí hậu. ===
Nằm trong vùng nhiệt đới gió mùa và là miền núi cao, khí hậu Hà Giang về cơ bản mang những đặc điểm của vùng núi Việt Bắc – Hoàng Liên Sơn, song cũng có những đặc điểm riêng, mát và lạnh hơn các tỉnh miền Đông Bắc, nhưng ấm hơn các tỉnh miền Tây Bắc.

Khí hậu tỉnh Hà Giang mang nét đặc trưng của khí hậu nhiệt đới gió mùa kết hợp với khí hậu á nhiệt đới vùng núi cao, có mùa đông lạnh kéo dài, lạnh nhất từ tháng XII đến tháng I năm sau. Mùa hè nóng, mưa nhiều, nóng nhất vào tháng VII và tháng VIII. 
- Nhiệt độ
Nhiệt độ trung bình năm tại khu vực thực hiện nhiệm vụ từ 21,8oC đến 23,6oC. Nhiệt độ tại khu vực thành phố Hà Giang và huyện Bắc Quang thường cao hơn khu vực huyện Bắc Mê và Hoàng Su Phì khoảng 1oC đến 2oC. 
Nhiệt độ trung bình tháng thấp nhất vào tháng I từ 14,5oC đến 19,5oC, nhiệt độ trung bình tháng cao nhất vào tháng VI, VII, VIII từ 25,9oC đến 35,6oC. Theo số liệu quan trắc nhiều năm, có những thời điểm về mùa đông nhiệt độ xuống rất thấp, nhất là vùng cao núi đá có khu vực xuất hiện băng, tuyết có những nơi nhiệt độ thấp nhất xuống tới -0,1oC đo được tại trạm Hoàng Su Phì ngày 27/12/1982. Nhiệt độ thấp nhất tại các trạm vào mùa đông thường nhỏ hơn 10oC. Nhiệt độ cao nhất đo được có thời điểm lên tới 41oC vào ngày 03/5/1994, nhiệt độ cao nhất ngày của các trạm ghi được khoảng 35,2oC đến 41oC.
- Độ ẩm
Hà Giang là một trong những vùng có độ ẩm cao ở hầu hết các mùa trong năm, độ ẩm bình quân năm là 77-88%, trong đó độ ẩm thấp nhất trung bình tháng là 71% vào tháng 3/1986 và tháng 4/2012 đo được tại trạm Hoàng Su Phì. Độ ẩm cao nhất là 99% vào tháng 10/1997. Độ ẩm cao diễn ra vào các tháng cuối mùa hạ (tháng VII và tháng VIII).
- Nắng
Số giờ nắng bình quân năm thời kỳ 1981-2019 cả tỉnh khoảng 1.586 giờ, trong năm số giờ nắng nhiều là năm 1981 với 2.241 giờ nắng đo được tại trạm Hà Giang và số giờ nắng ít là năm 2011 với 1.104 giờ đo được tại trạm Bắc Quang. Trong năm, tháng có giờ nắng nhiều nhất rơi vào tháng VII, tháng VIII với số giờ nắng lên tới 348,6 giờ vào tháng IX năm 2010. Tháng có số giờ nắng ít nhất là tháng I, tháng II với số giờ nắng trong tháng chỉ là 10,6 giờ vào tháng I năm 2013. 
- Gió
Hướng gió chính ở Hà Giang phụ thuộc vào địa hình thung lũng, gió trong các thung lũng thường yếu với tốc độ trung bình khoảng 1-1,3 m/s, trong đó tháng VII, tháng VIII là tháng có tốc độ gió lớn nhất: từ 20 m/s (trạm Hoàng Su Phì) đến 35 m/s (trạm Bắc Mê). 
- Mưa
Mùa mưa kéo dài từ tháng V đến cuối tháng IX và mùa khô bắt đầu từ tháng X đến tháng IV năm sau. Lượng mưa năm biến động rất mạnh so với yếu tố khí tượng khác, giá trị cực tiểu, cực đại của lượng mưa có thể chênh nhau từ hai đến ba lần. Xét theo không gian lượng mưa năm thời kỳ 1990-2019 thì trong khu vực dao động trong khoảng 1.200-4.600mm, trong đó tâm mưa lớn nhất là khu vực Bắc Quang, theo kết quả quan trắc lượng mưa tại trạm Bắc Quang thì với lượng mưa năm trung bình thời kỳ 1961-2019 khoảng 4.551mm, là một trong những tâm mưa lớn của khu vực, vào năm 1971 lượng mưa năm lớn nhất đạt 6.366mm. Lượng mưa nhiều nhất vào tháng VI và tháng VII. Địa phương có lượng mưa lớn nhất là huyện Bắc Quang có tháng tới 1.429mm và mưa ít nhất là huyện Hoàng Su Phì, có tháng chỉ 24,2mm. Ngoài ra, tỉnh Hà Giang còn có hiện tượng mưa phùn (32 ngày/năm) nhưng ít chịu ảnh hưởng trực tiếp từ bão. Tuy nhiên, vào mùa mưa dễ gây lũ quét, lũ ống, mưa đá làm ảnh hưởng không nhỏ đến đời sống và sinh hoạt của nhân dân địa phương.

=== Đặc điểm địa hình. ===
Do cấu tạo địa hình phức tạp, thiên nhiên tạo ra và ưu đãi cho Hà Giang một nguồn tiềm năng to lớn về khí hậu, đất đai, tài nguyên và khoáng sản... Từ những đặc điểm khí hậu, thổ nhưỡng, địa hình Hà Giang được chia thành ba vùng với những điều kiện tự nhiên, kinh tế và xã hội khác biệt, mỗi vùng có tiềm năng và thế mạnh riêng đó là:

"- Vùng I:" Là vùng cao núi đá phía Bắc gồm 4 huyện: Đồng Văn, Mèo Vạc, Yên Minh và Quản Bạ. Diện tích toàn vùng là 2.352,7 km², dân số trên 20 vạn người chiếm xấp xỉ 34,3% dân số toàn tỉnh. Do điều kiện khí hậu rét đậm về mùa đông, mát mẻ về mùa hè nên rất thích hợp với việc phát triển các loại cây ôn đới như cây dược liệu thảo quả, đỗ trọng; Cây ăn quả như mận, đào, lê, táo... Cây lương thực chính ở vùng này là cây ngô. Chăn nuôi chủ yếu là bò, dê, ngựa và nuôi ong. Những giống gia súc trên đây là giống riêng của vùng ôn đới, có đặc điểm to hơn và chịu được rét đến cả độ âm. Đàn ong ở đây chủ yếu chỉ phát triển vụ hè - thu với 2 loại hoa chính là hoa ngô và hoa bạc hà. Mật ong hoa bạc hà là  thứ mật ong đặc biệt có giá trị trong việc chữa bệnh và bồi dưỡng sức khoẻ.

"- Vùng II:" Là vùng cao núi đất phía tây gồm các huyện Hoàng Su Phì và Xín Mần. Diện tích tự nhiên 1.211,3 km², dân số chiếm 15,9%. Điều kiện tự nhiên vùng này thích hợp cho việc phát triển cây trẩu và cây thông lấy nhựa. Cây lương thực chính vùng này là lúa nước và ngô. Chăn nuôi chủ yếu là trâu, ngựa, dê và các loại gia cầm.Vùng này là vùng đất của chè Shan tuyết và chủ nhân lâu đời của nó là người Dao - Một dân tộc có kinh nghiệm trồng và chăm sóc cây chè núi lâu đời.

"- Vùng III:" Là vùng núi thấp gồm các huyện: Bắc Quang, Vị Xuyên, Bắc Mê, Quang Bình và thành phố Hà Giang là vùng trọng điểm kinh tế của Hà Giang. Diện tích tự nhiên 4.320,3 km², dân số chiếm 49,8%. Điều kiện tự nhiên thích hợp với các loại cây nhiệt đới, thuận lợi cho việc phát triển nghề rừng, trồng các loại cây nguyên liệu giấy như bồ đề, mỡ, thông và đây cũng là vùng tre, nứa, vầu, luồng lớn nhất trong tỉnh... Ngoài ra đây còn là vùng trồng các loại cây ăn quả có múi như cam, quýt, chanh...

=== Tài nguyên thiên nhiên. ===
a. Thổ nhưỡng

Thổ nhưỡng của Hà Giang rất phong phú với 9 nhóm đất chính, trong đó nhóm đất xám chiếm diện tích lớn nhất với 585.418 ha, chiếm 74,28% diện tích tự nhiên. Đây là nhóm đất rất thích hợp để trồng và phát triển các loại cây ăn quả (cam, quýt, lê, mận...), cây công nghiệp (chè, cà phê...), cây dược liệu (đỗ trọng, thảo quả, huyền sâm...). Các nhà khoa học đã xác định và phân chia các khu vực thổ nhưỡng chính của Hà Giang như sau:

- Khu vòm nâng sông Chảy, lớp thổ nhưỡng hình thành trên nền 2 nhóm đá chính là măcma axit và đá biến chất. Địa hình nơi đây được xếp vào kiểu núi khối tảng dạng vòm trên nền nguyên sinh phân cắt mạnh. Khu vực này có lượng mưa trung bình hàng năm khá lớn (3.000 mm). Với những điều kiện như vậy, đã tạo nên ở đây một lớp phủ thổ nhưỡng đa dạng, trong đó phần lớn là đất mùn màu vàng đỏ, phù hợp để phát triển những cánh rừng thuộc kiểu á nhiệt đới.

- Khu Quản Bạ - Bắc Mê, lớp thổ nhưỡng hình thành trên nền 3 nhóm đá chính là trầm tích đá hạt mịn bị biến chất, tướng đá lục hoặc  lục yếu tiếp đến là loại đá vôi hoặc sét vôi và đá lục nguyên hạt vừa và mịn. Địa hình ở đây được xếp vào kiểu núi khối tảng trên nền nguyên sinh, bị phân cắt rất mạnh. Đây cũng là khu vực có lượng mưa trung bình năm khá lớn (3.000 mm). Vì vậy, lớp phủ thổ nhưỡng ở đây đa phần là nhóm đất mùn màu vàng đỏ và mùn xám sẫm, tạo nên một thảm thực vật hết sức phong phú với những cánh rừng kiểu á nhiệt đới thường xanh.

Khu vực Đồng Văn - Mèo Vạc, lớp thổ nhưỡng hình thành trên nền đá vôi bị phân hoá mạnh, địa hình karst. Phần lớn lớp phủ thổ nhưỡng ở đây là loại đất đỏ xám hoặc vàng sẫm, với thảm thực vật chủ yếu là các loại cây thấp, mật độ thưa. Rừng ở khu vực này thường có các loại cây lấy gỗ thuộc nhóm tứ thiết như trai, nghiến...

- Khu tây bắc Vĩnh Tuy, lớp thổ nhưỡng hình thành trên cấu trúc địa chất của vòm nâng sông Chảy. Địa hình nơi đây có đặc trưng là các dải đồi, núi và gò thấp, sườn ít dốc. Khu vực này có lượng mưa lớn nhất cả nước, do vậy lớp phủ thổ nhưỡng ở đây chủ yếu là nhóm đất màu xám sẫm hơi đen, phù hợp với trồng cây ăn quả nhất là cam.

b. Tài nguyên khoáng sản

Căn cứ trên những cứ liệu về cấu trúc địa chất, các nhà khoa học đã dự báo rằng Hà Giang là một địa bàn có tiềm năng và triển vọng lớn về khoáng sản như sắt, mangan, chì, thiếc, antimon, vàng, đá quý...

Sắt ở dạng manhetit - hematit - sulfide đã từng thấy ở Tùng Bá - Bắc Mê. Cũng ở khu vực này còn có mỏ chì - kẽm. Ở vùng đông nam vòm nâng sông Chảy đã phát hiện các mỏ và điểm quặng mangan. Ơ Bắc Quang đã gặp các điểm quặng đồng (Cu - Ni) có nguồn gốc măcma. Ở khu vực từ Cao Bồ đến Việt Lâm có nhiều mạch quặng đa kim - vàng. Đồng thời dọc theo các bãi bồi nhất là từ chỗ gặp nhau giữa sông Lô và sông Gâm trở lên thượng nguồn là nơi có nhiều vàng sa khoáng. Ngoài ra, Hà Giang còn có một trữ lượng khá lớn các loại khoáng sản không kim loại như: Cao lanh, sét gốm, đá vôi, cát, sỏi, cát kết, đá phiến, laterit, granit, gabro, ryolit... và có cả than, trong đó quan trọng hơn cả là vỉa than Phó Bảng.

c. Tài nguyên rừng

Là một tỉnh vùng núi cao, núi đồi chiếm hơn 3/4 diện tích, môi trường thuận lợi cho thực vật tự nhiên cũng như rừng trồng phát triển. Rừng là thế mạnh kinh tế chủ yếu của Hà Giang và còn có ý nghĩa lớn vào khoa học và bảo vệ môi trường. Do đặc điểm địa hình, thổ nhưỡng, khí hậu, rừng Hà Giang khá phong phú và được coi là một trong những khu vực đặc trưng của kiểu loại rừng á nhiệt đới, với nhiều chủng loại. Diện tích đất rừng của Hà Giang thuộc vào loại lớn của cả nước. Diện tích có rừng tính đến 31/12/2005 là 345.860 ha, đất trống quy hoạch cho lâm nghiệp 262.918 ha.

Những năm gần đây, với những chủ trương, chính sách của nhà nước, biện pháp tích cực của địa phương trong triển khai chính sách giao đất, giao rừng, phủ xanh đất trống, đồi núi trọc, nên hàng năm tỉnh trồng thêm được từ 3.000 - 5.000 ha rừng tập trung, do đó đưa độ che phủ đạt 42,9% vào cuối năm 2005. Điều đó không những có tác dụng chống xói mòn đất bề mặt, mà vành đai rừng phòng hộ đầu nguồn đã khống chế phần nào lũ lụt, bảo vệ môi trường sinh thấy. Rừng còn cung cấp nguồn nguyên liệu quan trọng cho công nghiệp giấy, vật tư xây dựng...

Người ta đã từng phát hiện ở rừng Hà Giang có nhiều loại động vật quý hiếm như: hổ, báo gấm, vọc má trắng, gấu ngựa, lợn rừng, khỉ, hoẵng... Riêng khu vực Tây Côn Lĩnh đã thống kê được 47 loài thú, 140 loài chim thuộc 25 bộ, 75 họ. Rừng xã Phong Quang (Vị Xuyên) được xếp vào hệ thống các khu bảo tồn thiên nhiên điển hình của hệ rừng núi đá vùng Đông Bắc Việt Nam, với hệ động thực vật rừng phong phú và có giá trị kinh tế cao.

d. Tài nguyên thủy sản

Tuy là một tỉnh miền núi không có thế mạnh về thuỷ sản nhưng ở khu vực Hà Giang lại có thể tìm thấy những loài thuỷ sản quý, hiếm, có giá trị đặc biệt. Trên lưu vực sông Gâm có thể tìm thấy các loại tôm, cua, cá chỉ có ở khu vực nguồn sông có nhiều ghềnh đá. Đặc biệt ở đây có loại cá Dầm xanh, cá Anh vũ ngon nổi tiếng, đã từng là những loại đặc sản cúng tiến cung đình. Trên sông Lô, cũng có một số loài cá, tôm theo nguồn nước sông Hồng ngược lên và được coi là đặc sản ở sông Lô như: cá chép, cá bống, cá măng, ba ba...

Phát huy nguồn lợi thuỷ sản, những năm gần đây, ở nhiều nơi nhân dân đã biết tận dụng mặt nước, các đầm, ao, hồ để chăn thả các loại tôm cá có thời gian sinh trưởng ngắn, năng suất cao. Một số nơi bà con nông dân còn kết hợp trồng lúa và thả cá trên những chân ruộng nước.  Nhiều trang trại của họ đã phát triển theo mô hình VACR (vườn, ao, chuồng, rừng) đem lại hiệu quả kinh tế rõ rệt.

== Lịch sử. ==
Vào thời Hùng Vương, mảnh đất Hà Giang đã là một trong 15 bộ của quốc gia Lạc Việt. Thời Thục Phán An Dương Vương lập nước Âu Lạc, Hà Giang thuộc bộ lạc Tây Vu.

Trong thời kỳ đô hộ của phong kiến phương Bắc kéo dài nghìn năm, khu vực Hà Giang vẫn nằm trong địa phận huyện Tây Vu thuộc quận Giao Chỉ.

Từ năm 1075 (đời nhà Lý). Miền đất Hà Giang lúc đó thuộc về châu Bình Nguyên.

Vào đầu đời Trần, khu vực Hà Giang, Tuyên Quang lúc đó gọi là châu Tuyên Quang thuộc lộ Quốc Oai. Năm 1397 đổi thành trấn Tuyên Quang.

Địa danh Hà Giang lần đầu tiên được nhắc đến trong bài minh khắc trên chuông chùa Sùng Khánh (xã Đạo Đức, Vị Xuyên), được đúc nhân dịp trùng tu chùa vào đầu thời Vua Lê Dụ Tông tức năm Ất Dậu 1707.

Năm Minh Mệnh thứ 16 (năm 1835), nhà Nguyễn bỏ châu Bảo Lạc, chia làm hai huyện: Vĩnh Điện (khoảng Bắc Mê, Yên Minh và một phần Quản Bạ ngày nay và huyện Để Định (khoảng huyện Bảo Lạc, Cao Bằng và một phần Đồng Văn, Mèo Vạc ngày nay). Lấy sông Lô phân giới để chia châu Vị Xuyên thành hai đơn vị hành chính mới: Khu vực phía hữu ngạn sông Lô được gọi là huyện Vĩnh Tuy, còn phía tả ngạn sông Lô là huyện Vị Xuyên.

Năm Thiệu Trị thứ hai (năm 1842), triều đình nhà Nguyễn chia Tuyên Quang làm ba hạt: Hà Giang, Bắc Quang, Tuyên Quang. Hạt Hà Giang có một phủ là Tương Yên với bốn huyện: Vị Xuyên, Vĩnh Tuy, Vĩnh Điện, Để Định.

Năm Thiệu Trị thứ tư (năm 1844), nhà Vua lại phê chuẩn cho các huyện châu thuộc tỉnh hạt biên giới phía Bắc, Tây Bắc, trong đó có Hà Giang, "vẫn theo như cũ đặt chức thổ quan". Đến đời Tự Đức thì chế độ "thổ quan" bị bãi bỏ trên phạm vi cả nước.

Năm 1858, sau khi đánh chiếm hầu hết các tỉnh Nam Kỳ, Bắc Kỳ.

Năm 1887, thực dân Pháp đánh chiếm Hà Giang và thay đổi chế độ cai trị bằng cách thiết lập các đạo quan binh.

Ngày 20 tháng 8 năm 1891, tỉnh Hà Giang được thành lập, bao gồm phủ Tương Yên và huyện Vĩnh Tuy (tỉnh Tuyên Quang).

Năm 1893, trong dịp cải tổ trong các quân khu, Hà Giang trở thành trung tâm của một quân khu và cùng với Tuyên Quang hợp thành Đạo quan binh thứ ba (quân khu 3).

Ngày 17 tháng 9 năm 1895, Toàn quyền Đông Dương ra Quyết định số 1432 chia khu quân sự thứ ba thành ba tỉnh: Tuyên Quang, Bắc Quang và Hà Giang. Trong đó, Hà Giang bao gồm huyện Vị Xuyên (trừ tổng Phú Loan và Bằng Hành), cộng thêm các tổng Phương Độ và Tương Yên.

Ngày 28 tháng 4 năm 1904, Toàn quyền Đông Dương lại ra quyết định sáp nhập tỉnh Bắc Quang và tỉnh Hà Giang thành Đạo quan binh Hà Giang. Đến thời điểm này, Đạo quan binh thứ ba Hà Giang đã được xác định ranh giới rõ ràng và tương đối ổn định.

Trước Cách mạng tháng Tám năm 1945, Hà Giang có 4 châu Bắc Quang, Vị Xuyên, Đồng Văn, Hoàng Su Phì và thị xã Hà Giang.

Ngày 23 tháng 3 năm 1959, Chủ tịch Hồ Chí Minh ký sắc lệnh giải tán Khu Lao - Hà - Yên, sáp nhập tỉnh Hà Giang vào Khu tự trị Việt Bắc.

Ngày 15 tháng 12 năm 1962, Hội đồng Chính phủ ban hành Quyết định số 211/QĐ-CP<ref name="211/1962/QĐ-CP">Quyết định số 211/QĐ-CP năm 1962 của Hội đồng Chính phủ</ref> về việc:
BULLET::::- Chia huyện Đồng Văn thành 3 huyện: Đồng Văn, Mèo Vạc và Yên Minh
BULLET::::- Chia huyện Vị Xuyên thành 2 huyện: Vị Xuyên và Quản Bạ.

Ngày 1 tháng 4 năm 1965, Hội đồng Chính phủ ban hành Quyết định số 49–CP<ref name="49/1965/QĐ–HĐCP">Quyết định số 49–CP năm 1965 của Hội đồng Chính phủ</ref> về việc chia huyện Hoàng Su Phì thành 2 huyện: Hoàng Su Phì và Xín Mần.

Tháng 12 năm 1974, tỉnh Hà Tuyên được thành lập trên cơ sở hợp nhất hai tỉnh Hà Giang và Tuyên Quang.

Ngày 14 tháng 5 năm 1981, Hội đồng Chính phủ ban hành Quyết định 185/1981/QĐ-CP<ref name="185/1981/QĐ-CP"></ref> về việc điều chỉnh địa giới một số xã thuộc các huyện Mèo Vạc, Quản Bạ, Vị Xuyên, Hoàng Xu Phì, Xín Mần.

Ngày 21 tháng 12 năm 1982, Hội đồng Bộ trưởng ban hành Quyết định 179-HĐBT về việc điều chỉnh địa giới các huyện Yên Minh, Mèo Vạc và Đồng Văn.

Ngày 18 tháng 11 năm 1983, Hội đồng Bộ trưởng ban hành Quyết định 136-HĐBT<ref name="136/1983/QĐ-HĐBT"></ref> về việc điều chỉnh địa giới một số huyện thuộc tỉnh Hà Tuyên:
BULLET::::- Chia huyện Vị Xuyên thành 2 huyện: Vị Xuyên và Bắc Mê
BULLET::::- Điều chỉnh địa giới các huyện Vị Xuyên, Xín Mần, Hoàng Su Phì, Bắc Quang.

Ngày 19 tháng 2 năm 1986, Hội đồng Bộ trưởng ban hành Quyết định số 14-HĐBT về việc chia tách một số xã, thị trấn thuộc huyện Bắc Quang, tỉnh Hà Tuyên.

Ngày 13 tháng 2 năm 1987, Hội đồng Bộ trưởng ban hành Quyết định 28-HĐBT về việc chia một số xã và thành lập thị trấn của các huyện Bắc Mê, Na Hang và Yên Sơn thuộc tỉnh Hà Tuyên.

Ngày 12 tháng 8 năm 1991, tại kỳ họp thứ 9 khoá VIII, Quốc hội nước Cộng hoà xã hội chủ nghĩa Việt Nam đã quyết định chia tỉnh Hà Tuyên thành hai tỉnh Hà Giang và Tuyên Quang. Tỉnh Hà Giang được tái lập gồm 10 đơn vị hành chính là thị xã Hà Giang và 9 huyện, tỉnh lỵ đặt tại thị xã Hà Giang.

Ngày 29 tháng 8 năm 1994, Chính phủ ban hành Nghị định số 112/1994/NĐ-CP<ref name="112/1994/NĐ-CP">Nghị định số 112-CP năm 1994 của Chính phủ</ref> về việc:
BULLET::::- Thành lập một số phường, xã, thị trấn thuộc thị xã Hà Giang và các huyện Vị Xuyên, Bắc Quang
BULLET::::- Điều chỉnh địa giới huyện Hoàng Su Phì và huyện Xín Mần.

Ngày 29 tháng 1 năm 1997, Chính phủ ban hành Nghị định 8-CP<ref name="8/1997/NĐ-CP"></ref> về việc chia tách một số xã thuộc các huyện Yên Minh, Bắc Quang và Vị Xuyên thuộc tỉnh Hà Giang.

Ngày 20 tháng 8 năm 1999, Chính phủ ban hành Nghị định 74/1999/NĐ-CP<ref name="74/1999/NĐ-CP"></ref> về việc điều chỉnh địa giới hành chính để thành lập thị trấn và xã thuộc các huyện Mèo Vạc, Yên Minh, Quản Bạ, Bắc Quang, Hoàng Su Phì và thị xã Hà Giang, tỉnh Hà Giang.

Ngày 1 tháng 12 năm 2003, Chính phủ ban hành Nghị định 146/2003/NĐ-CP <ref name="146/2003/NĐ-CP"></ref> về việc:
BULLET::::- Chia tách một số xã thuộc huyện Bắc Quang
BULLET::::- Thành lập huyện Quang Bình được thành lập trên cơ sở tách một phần thuộc huyện Bắc Quang
BULLET::::- Thành lập các xã thuộc huyện Hoàng Su Phì và huyện Xín Mần.

Ngày 9 tháng 8 năm 2005, Chính phủ ban hành Nghị định 104/2005/NĐ-CP<ref name="104/2005/NĐ-CP"></ref> về việc điều chỉnh địa giới hành chính, thành lập phường, xã thuộc thị xã Hà Giang và huyện Mèo Vạc, tỉnh Hà Giang.

Ngày 23 tháng 6 năm 2006, Chính phủ ban hành Nghị định 64/2006/NĐ-CP<ref name="64/2006/NĐ-CP"></ref> về việc điều chỉnh địa giới thị xã Hà Giang và huyện Vị Xuyên, tỉnh Hà Giang.

Ngày 31 tháng 3 năm 2009, Chính phủ ban hành Nghị định số 11/NĐ-CP<ref name="11/2009/NĐ-CP"></ref> về việc thành lập các thị trấn huyện lỵ tại các huyện Đồng Văn, Bắc Mê và Xín Mần thuộc tỉnh Hà Giang.

Ngày 27 tháng 9 năm 2010, Thủ tướng Chính phủ đã ban hành Nghị quyết số 35/NQ-CP<ref name="35/2010/NQ-CP"></ref> về việc thành lập thành phố Hà Giang thuộc tỉnh Hà Giang trên cơ sở toàn bộ thị xã Hà Giang.

Ngày 1 tháng 1 năm 2020, Uỷ ban Thường vụ Quốc hội ban hành Nghị quyết số 827/NQ-UBTVQH14<ref name="827/NQ-UBTVQH14"></ref> về việc sắp nhập một số xã thuộc các huyện Hoàng Su Phì, Xín Mần thuộc tỉnh Hà Giang:
BULLET::::- Sáp nhập toàn bộ xã Bản Péo thuộc huyện Hoàng Su Phì vào xã Nậm Dịch
BULLET::::- Sáp nhập toàn bộ xã Ngán Chiên thuộc huyện Xín Mần vào xã Trung Thịnh.

== Hành chính. ==
Tỉnh Hà Giang có 11 đơn vị hành chính cấp huyện, bao gồm 1 thành phố và 10 huyện với 193 đơn vị hành chính cấp xã, bao gồm 5 phường, 13 thị trấn và 175 xã.

Đến năm 2012, tỉnh Hà Giang có 2.069 thôn, tổ dân phố. Toàn bộ các đơn vị hành chính của Hà Giang đều thuộc khu vực miền núi.

== Dân cư. ==
Dân số tỉnh Hà Giang theo điều tra dân số ngày 1/4/2019 là 854.679 người. Trong đó, dân số thành thị là 135.465 người (chiếm khoảng 15,8% dân số). So với các tỉnh miền núi phía Bắc khác thì dân số Hà Giang tương đối đông.

Các dân tộc: H'Mông (chiếm 32,9% tổng dân số toàn tỉnh), Tày (23,2 %), Dao (14,9 %), Việt (12,8 %), Nùng (9,7 %)...

Tính đến ngày 1 tháng 4 năm 2019, toàn tỉnh có 7 tôn giáo khác nhau đạt 40.393 người, nhiều nhất là đạo Tin Lành có 35.960 người, tiếp theo là Công giáo đạt 4.110 người, Phật giáo có 290 người. Còn lại các tôn giáo khác như Hồi giáo có 26 người, đạo Cao Đài có ba người, Phật giáo Hòa Hảo có ba người và 1 người theo Minh Lý đạo.

== Du lịch. ==
BULLET::::- Cao nguyên đá Đồng Văn nằm trải rộng trên bốn huyện Quản Bạ, Yên Minh, Đồng Văn, Mèo Vạc được công nhận là Công viên địa chất Toàn cầu vào năm 2010. Đây là một trong những vùng đá vôi đặc biệt, chứa đựng những dấu ấn tiêu biểu về lịch sử phát triển vỏ Trái Đất, những hiện tượng tự nhiên, cảnh quan đặc sắc về thẩm mỹ, tính đa dạng sinh học cao và truyền thống văn hóa lâu đời của cộng đồng cư dân bản địa như các dân tộc Mông, Lô Lô, Pu Péo, Dao. Cao nguyên đá cũng là nơi có nhiều di tích danh thắng quốc gia đã được công nhận như: Di tích kiến trúc nhà Vương, Cột cờ Lũng Cú, phố cổ Đồng Văn, động Én, đèo Mã Pì Lèng, núi Đôi Quản Bạ v.v.. Đồng Văn còn nổi tiếng về các loại hoa quả: đào, mận, lê, táo, hồng... về dược liệu: tam thất, thục địa, đại hồi, quế chi...
BULLET::::- Hệ thống các hang động: Hang Phương Thiện: cách thành phố Hà Giang 7 km (4,38 dặm) xuôi về phía nam. Đây là nơi có nhiều phong cảnh, nhiều hang động tự nhiên.Động Tiên và Suối Tiên nằm cách thành phố Hà Giang 2 km (1.25 dặm). Nhân dân quanh vùng vẫn thường đến Động Tiên lấy nước và cầu may mắn vào lúc giao thừa.. Hang Chui: cách thành phố Hà Giang 7 km (4,38 dặm) về phía nam. Hang ăn sâu vào lòng núi khoảng 100 m (300 ft). Cửa hang hẹp phải lách người mới qua được. Vào trong lòng hang mở rộng, vòm hang cao vút, nhiều nhũ đá. Hang có nhiều dơi, có dòng suối dâng cao đổ xuống thành thác.
BULLET::::- Dinh thự họ Vương thuộc xã Sà Phìn là một công trình kiến trúc đẹp và độc đáo được xếp hạng cấp quốc gia năm 1993. Đường dẫn vào dinh được lát bằng những phiến đá lớn vuông vức, phẳng lỳ. Dinh được bao bọc bởi hai vòng tường thành xây bằng đá hộc. Dinh thự được xây dựng chủ yếu bằng đá xanh, gỗ pơ-mu, ngói đất nung già, các chi tiết được chạm trổ tỉ mỉ, công phu, đẹp mắt, được xây theo cấu trúc hình chữ "vương", tọa lạc trên quả đồi hình mai rùa. Đây là một điển hình về sự giao thoa nghệ thuật kiến trúc của người Mông và người Hán ở khu vực biên giới Việt – Trung.
BULLET::::- Chợ tình Khau Vai họp mỗi năm một lần vào ngày 27 tháng 3 âm lịch tại xã Khau Vai, huyện Mèo Vạc. Bắt nguồn từ 1 câu chuyện tình, Khau Vai trở thành nơi hò hẹn chung cho tất cả những người yêu nhau trong vùng. Chợ Khau Vai ban đầu họp không có người mua, không có người bán. Khoảng mười năm trở lại đây, do nhu cầu cuộc sống nên ngày chợ họp ngoài việc hò hẹn, gặp gỡ, người ta mang cả hàng hóa đến bán ở chợ. Do vậy đến chợ Khau Vai, người ta cũng có thể mua, bán, trao đổi những sản vật vùng cao.
BULLET::::- Tiểu khu Trọng Con Cách đường quốc lộ số 2, 20 km về phía đông nam, cách Thành phố Hà Giang khoảng 60 km về phía bắc ở tại Xã Bằng Hành, huyện Bắc Quang, Tỉnh Hà Giang (đã được Nhà nước xếp hạng là di tích lịch sử năm 1996). Đây được xem là cái nôi của phong trào cách mạng ở Hà Giang .
BULLET::::- Chùa Sùng Khánh cách Thành phố Hà Giang 9 km về phía nam thuộc thôn Làng Nùng, xã Đạo Đức, huyện Vị Xuyên,được nhà nước xếp hạng là di tích lịch sử nghệ thuật năm 1993. Chùa được xây dựng thời Triệu Phong (1356), do thời gian, chùa bị hư hại, đến năm 1989 được nhân dân xây dựng trên nền chùa cũ. Ở đây còn lưu giữ hai di vật: Bia đá thời Trần (1367) ghi lại công lao của người sáng lập ra chùa và một quả Chuông cao 0.90 m, đường k ính 0.67 m, được đúc thời Hậu Lê (1705). Nghệ thuật khắc trên đá, trên Chuông đồng và kỹ thuật đúc Chuông là một bằng cứ nói lên bàn tay tinh xảo của các nghệ nhân vùng biên giới phía bắc này, và từ đó biết thêm lịch sử phát triển thời Trần và Lê tới tận vùng biên ải Hà Giang.
BULLET::::- Bãi đá cổ Nấm Dẩn thuộc xã Nấm Dẩn, huyện Xín Mần cách trung tâm huyện lỵ 15 km về phía nam. Tại đây đã thống kê được hơn 80 hình khắc về bàn chân, tay người, ruộng bậc thang và nhiều hình học khác trên đá. Các nhà khoa học bước đầu xác định các hình khắc này xuất hiện từ hơn hai nghìn năm trước. Đây là nguồn tư liệu quý về những cư dân Việt cổ ở vùng đất Hà Giang.
BULLET::::- Chùa Bình Lâm thuộc địa phận thôn Tông Mường xã Phú Linh, Thành phố Hà Giang. Chùa còn có tên gọi chữ Hán là "Bình Lâm Tự". Nhân dân ở đây còn lưu giữ một quả chuông thời Trần được đúc vào tháng 3 năm Ất Mùi (1295) chuông có chiều cao 103 cm, đường kính miệng 65 cm, quai được cấu tạo bởi hai hình rồng, trên chuông có khắc bài Minh bằng chữ Hán gồm 309 chữ năm Bính Thân, niên hiệu Hưng Long thứ 4 (1296). Trên quả chuông ta bắt gặp tiêu bản rồng nổi trên chất liệu đồng (thế kỷ 13). Cùng với quả chuông, tại chùa Bình Lâm còn phát hiện được một số di vật như Tháp đất nung, mái ngói có hoạ tiết hoa chanh...là những nét quen thuộc và tiêu biểu của văn hoá thời Trần.

== Lễ hội. ==
Hà Giang là nơi có nhiều sản phẩm văn hóa đặc sắc từ truyền thống lâu đời của hơn 20 dân tộc, một địa danh du lịch đáng nhớ bởi cảnh quan thiên nhiên và con người ở đây. Không giống với bất kỳ một nơi du lịch nào ở Việt Nam, đến Hà Giang, du khách có thể thấy được những sản phẩm kết tinh từ truyền thống văn hóa độc đáo của người miền núi, đó là các loại khăn thêu, túi vải, áo váy với các loại hoa văn rực rỡ. Du khách sẽ tham dự những phiên chợ vùng cao đầy thơ mộng.

Lễ mừng nhà mới dân tộc Lô Lô: Lễ mừng nhà mới kéo dài khoảng 2 ngày 2 đêm ở ngôi nhà mới của người dân tộc Lô Lô. Cả bản kéo tới ăn mừng cho ngôi nhà mới. Thầy cúng đi hát, sau đó cùng ăn uống vui chơi, hòa tấu kèn sáo và hát giao duyên nam nữ.

Lễ hội mùa xuân: Đây là lễ hội vui xuân của dân tộc H'mông và dân tộc Dao, thường được tổ chức vào những ngày sau Tết Nguyên Đán và kéo dài từ 3 đến 7 ngày. Lễ hội mang tính chất tổng hợp mừng công, cầu mưa, cầu con trai. Lễ hội có thi bắn nỏ, hát giao duyên, ném pa páo, uống rượu, mở tiệc đãi khách.

Lễ hội vỗ mông của dân tộc Mông: Ngày mùng 5 Tết Nguyên Đán hằng năm, cái chàng trai, cô gái đổ về Mèo Vạc nhằm tìm cho mình vợ (chồng). Khi tham gia lễ hội, các chàng trai, cô gái tìm đối tượng mà họ cảm thấy phù hợp với mình rồi vỗ mông đối tượng và chờ "đối phương" đáp lại. Đáng buồn, tục lệ tảo hôn vẫn tiếp diễn trong lễ hội này.

Lễ hội nhảy lửa của người Pà Thẻn: Lễ hội được tổ chức vào buổi tối ngày cuối năm. Bên đống lửa hồng có nhiều nghi lễ như mừng mùa, cầu thần linh phù hộ cho năm mới. Tại đây có nhiều người nhảy qua đống lửa, than. Trước đó họ đã được thầy mo cúng "nhập hồn" với sức mạnh của thần linh.

== Kinh tế. ==
Tổng thu ngân sách trên địa bàn tỉnh năm 2018 ước đạt 2.033 tỉ đồng.

Hà Giang là vùng miền núi nên dân số ít, mật độ dân số thấp, người Mông chiếm đa số, còn lại là các sắc dân gồm Thổ, La Chí, Tày, Dao, Mán, Nùng, Giáy và Lô Lô... Phần đông đều thờ cúng tổ tiên, thần linh; và đều có những sắc thái văn hóa đặc thù.

Cũng vì địa thế toàn rừng núi nên kinh tế Hà Giang tương đối kém phát triển. Lâm sản chính là vài loại gỗ quý như lát hoa, lát da đồng; và các loại gỗ cứng như lim, sến, trai, táu, đinh. Củ nâu, vầu, nứa ở đâu cũng có. Nông sản gồm lúa, ngô, khoai và các loại đậu đỗ. Vùng chân núi Tây Côn Lĩnh trồng nhiều trà. Dân chúng cũng trồng cây ăn trái, mận và lê ở vùng Đồng Văn, Hoàng Su Phì rất nổi tiếng. Nghề nuôi ong lấy mật khá thịnh hành. Rừng Hà Giang có nhiều động vật hoang dã như trăn, rắn, chim công, chim trĩ...

Khoáng sản có quặng sắt, mỏ chì, đồng, thủy ngân và cát trộn vàng. Sông Năng và Bảo Lạc có các kỹ nghệ lọc vàng nhưng vẫn còn thô sơ, ngoài ra chỉ toàn những tiểu công nghệ sản xuất vật dụng hàng ngày. Nền thương mại Hà Giang chỉ giới hạn ở sự trao đổi lâm sản với miền xuôi và với Trung Quốc.

Các vùng núi thấp như Vị Xuyên, Bắc Quang có kinh tế phát triển hơn vùng núi. Dựa vào sông Lô và lượng mưa lớn, các ngành nông nghiệp ở khu vực này rất phát triển, không kém gì vùng núi trung du. Nơi đây có vùng trồng cam sành nổi tiếng, những cánh đồng phì nhiêu...

Rải rác từ Vĩnh Tuy lên đến Vị Xuyên là các nhà máy sản xuất trà, đặc sản của Hà Giang có trà Shan tuyết cổ thụ (xã Cao Bồ). Đặc điểm trà Shan Tuyết là sạch sẽ, không có thuốc trừ sâu và thuốc kích thích, các nhà máy sản xuất trà hiện nay còn khuyến khích nhân dân trong vùng trồng xen kẽ cây gừng giữa các luống trà. Trà Shan tuyết cổ thụ của Hà Giang thường được xuất khẩu sang thị trường Đài Loan, Nhật Bản và một số nước Tây Âu, chưa thịnh hành trong thị trường nội địa như trà Tân Cương - Thái Nguyên.

== Giao thông. ==
=== Đường bộ. ===
Hà Giang có Quốc lộ 279 (nối các tỉnh miền núi phía Bắc là Quảng Ninh, Bắc Giang, Lạng Sơn, Bắc Kạn, Tuyên Quang, Hà Giang, Lào Cai, Lai Châu, Sơn La và Điện Biên với nhau) Đoạn cuối quốc lộ 279, từ chỗ giao với quốc lộ 6 đến cửa khẩu quốc tế Tây Trang là một phần của đường Xuyên Á AH13.

=== Biển số xe cơ giới. ===
Biển số xe mô tô tỉnh Hà Giang được quy định cụ thể đối với từng huyện:

- Thành phố. Hà Giang: 23B1

- Huyện Bắc Quang: 23D1

- Huyện Quang Bình: 23E1

- Huyện Hoàng Su Phì: 23F1

- Huyện Xín Mần: 23G1

- Huyện Vị Xuyên: 23H1

- Huyện Bắc Mê: 23K

- Huyện Mèo Vạc: 23P1

- Huyện Đồng Văn: 23N1

- Huyện Yên Minh: 23M1

- Huyện Quản Bạ: 23L1

== Liên kết ngoài. ==
BULLET::::- Trang chủ của tỉnh Hà Giang
"""
    formated_txt = remove_links(TXT)
    formated_txt = remove_newlines_tabs(formated_txt)
    formated_txt = removing_special_characters(formated_txt)
    # formated_txt = lower_casing_text(formated_txt)
    formated_txt = remove_whitespace(formated_txt)
    print(formated_txt)
if __name__=='__main__':
    main()