HAANCARE_URL = 'https://www.hanisamall.kr/admin'

SHIPPED_BEGIN_LIST_PAGE_URL = "https://haancare1.cafe24.com/admin/php/shop1/s_new/shipped_begin_list.php"
SHIPPED_END_LIST_PAGE_URL = 'https://haancare1.cafe24.com/admin/php/shop1/s/shipped_end_list.php'

SHIPPED_STANDBY_LIST_ORD_NUM_URL = "https://haancare1.cafe24.com/admin/php/shop1/s_new/shipped_standby_list_ord_num.php"
SHIPPED_COMPLETE_LIST_ORD_NUM_URL = "https://haancare1.cafe24.com/admin/php/shop1/s_new/shipped_complete_list_ord_num.php"
SODAM_SOFT_URL = "https://haancare.sodamsoft.com/orderlistall"

def getPaymentListURL(shop):
    return f"https://haancare1.cafe24.com/admin/php/{shop}/s/payment_list.php"