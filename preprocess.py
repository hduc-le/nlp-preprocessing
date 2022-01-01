import utils
import re
from underthesea import word_tokenize

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
    # Formatted_Text = re.sub(r"[^a-z0-9A-Z_ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂưăạảấầẩẫậắằẳẵặẹẻẽềềểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳỵỷỹ:$-,%.?!]+", ' ', text) 
    Formatted_Text = re.sub("\W+",' ', text)
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
    Formatted_Text = re.sub(r"[^a-zA-Z_ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂưăạảấầẩẫậắằẳẵặẹẻẽềềểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳỵỷỹ:$-,%.?!]+", ' ', text)
    return Formatted_Text

# The code for removing stopwords
stoplist = utils.load_txt_line_by_line('vietnamese-stopwords.txt')
stoplist = set(stoplist)

def removing_vietnamese_stopwords(text):
    """This function will remove stopwords which doesn't add much meaning to a sentence 
       & they can be remove safely without comprimising meaning of the sentence.
    
    arguments:
         input_text: "text" of type "String".
         
    return:
        value: Text after omitted all stopwords.
        
    Example: 
    Input : như vậy là hôm nay chúng ta đã hoàn thành tất cả công việc.
    Output : hôm nay đàn hoàn thành công việc 
    
   """
    # repr() function actually gives the precise information about the string
    text = repr(text)
    # Text without stopwords
    No_StopWords = [word for word in word_tokenize(text) if word.lower() not in stoplist ]
    # Convert list of tokens_without_stopwords to String type.
    words_string = ' '.join(No_StopWords)
    return words_string

def main():
    pass

if __name__=='__main__':
    main()