# coding: utf-8
import uiautomator2 as u2
def ordercondiction(standard_price,direction,openclose,setsell):
    d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/to_condition_order").click()
    # 触发价符号
    if setsell == "time":
        d.xpath('//*[@resource-id="com.shinnytech.futures.kuaiqixiaoq.release:id/spinner_trigger_way"]/android.widget.LinearLayout[1]/android.widget.TextView[2]').click()
        d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/tv_spinner_condition", text="时间触发").click()
        # 挑时间
        d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/textView_trigger_time").click()
        d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/mdtp_ok").click()   
        ###设定 交易结束前一分钟  14：58：57
        d.click(0.661, 0.492)
        d.click(0.441, 0.424)
        d.click(0.415, 0.419)
        d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/mdtp_ok").click()
    else:
        d.xpath('//*[@resource-id="com.shinnytech.futures.kuaiqixiaoq.release:id/spinner_trigger_price_range"]/android.widget.LinearLayout[1]/android.widget.TextView[2]').click()
        d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/tv_spinner_condition", text="≤").click()
        ###价格触发输入
        d.xpath('//*[@resource-id="com.shinnytech.futures.kuaiqixiaoq.release:id/spinner_trigger_way"]/android.widget.LinearLayout[1]/android.widget.TextView[2]').click()
        d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/tv_spinner_condition", text="价格触发").click()
    # 触发价输入
        d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/editText_trigger_order_price").click()
        d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/editText_trigger_price").set_text(standard_price) 
    ###买开
    d.xpath('//*[@resource-id="com.shinnytech.futures.kuaiqixiaoq.release:id/spinner_trigger_order_direction"]/android.widget.LinearLayout[1]/android.widget.TextView[2]').click()
    if direction == "买":
        d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/tv_spinner_condition", text="买").click()
    else:
        d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/tv_spinner_condition", text="卖").click()
    ###开平
    
    d.xpath('//*[@resource-id="com.shinnytech.futures.kuaiqixiaoq.release:id/spinner_trigger_order_offset"]/android.widget.LinearLayout[1]/android.widget.TextView[2]').click()
    if direction == "平":
        d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/tv_spinner_condition", text="平").click()
    else:
         d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/tv_spinner_condition", text="开").click()
    ###出发报价单
    d.xpath('//*[@resource-id="com.shinnytech.futures.kuaiqixiaoq.release:id/spinner_trigger_order_price"]/android.widget.LinearLayout[1]/android.widget.TextView[2]').click()
    d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/tv_spinner_condition", text="市价").click()
    
    ###出发报价单量
    d.xpath('//*[@resource-id="com.shinnytech.futures.kuaiqixiaoq.release:id/spinner_trigger_order_volume"]/android.widget.LinearLayout[1]/android.widget.TextView[2]').click()
    d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/tv_spinner_condition", text="指定").click()
    
    ### 挂单保存
    d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/trigger_save").click()    
def buy_in_openprice():
# trade if the needed
    #check volume
    d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/volume").click()
    #set the volum to 1
    d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/bid_open_position").click()
    d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/back_account").click()
    
    d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/bid_open_position").click()
    d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/order_ok").click()
#
###挂单
#d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/to_condition_order").click()
#
#
## 触发价符号
#d.xpath('//*[@resource-id="com.shinnytech.futures.kuaiqixiaoq.release:id/spinner_trigger_price_range"]/android.widget.LinearLayout[1]/android.widget.TextView[2]').click()
#d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/tv_spinner_condition", text="≤").click()
###触发方式
#d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/to_condition_order").click()
####价格触发输入
#d.xpath('//*[@resource-id="com.shinnytech.futures.kuaiqixiaoq.release:id/spinner_trigger_way"]/android.widget.LinearLayout[1]/android.widget.TextView[2]').click()
#d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/tv_spinner_condition", text="价格触发").click()
#
## 触发价输入
#d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/editText_trigger_order_price").click()
#d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/editText_trigger_price").set_text(standard_price)
#
####买开
#d.xpath('//*[@resource-id="com.shinnytech.futures.kuaiqixiaoq.release:id/spinner_trigger_order_direction"]/android.widget.LinearLayout[1]/android.widget.TextView[2]').click()
#d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/tv_spinner_condition", text="买").click()
####开平
#
#d.xpath('//*[@resource-id="com.shinnytech.futures.kuaiqixiaoq.release:id/spinner_trigger_order_offset"]/android.widget.LinearLayout[1]/android.widget.TextView[2]').click()
#d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/tv_spinner_condition", text="平").click()
####出发报价单
#d.xpath('//*[@resource-id="com.shinnytech.futures.kuaiqixiaoq.release:id/spinner_trigger_order_price"]/android.widget.LinearLayout[1]/android.widget.TextView[2]').click()
#d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/tv_spinner_condition", text="市价").click()
#
####出发报价单量
#d.xpath('//*[@resource-id="com.shinnytech.futures.kuaiqixiaoq.release:id/spinner_trigger_order_volume"]/android.widget.LinearLayout[1]/android.widget.TextView[2]').click()
#d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/tv_spinner_condition", text="全部").click()
#
#### 挂单保存
#d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/trigger_save").click()
if __name__ == '__main__':
    standard_price="3836.5"
    d = u2.connect('0.0.0.0')
    #d=u2.connect_wifi('192.168.4.165')
    d.app_start("com.shinnytech.futures.kuaiqixiaoq.release")
    d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/title_toolbar").click()
    d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/tv_id_dialog", text="主力合约").click()
    d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/quote_name").click()
    d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/rb_transaction_info").click()
    #ordercondiction(standard_price,"买","开")
    buy_in_openprice()
    #ordercondiction(standard_price,"买","平","time")
    d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/to_condition_order").click()
    d.click(0.899, 0.145)
    d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/tv_spinner_condition", text="时间触发").click()
    # 挑时间
    d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/textView_trigger_time").click()
    d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/mdtp_ok").click()   
    ###设定 交易结束前一分钟  14：58：57
    d.click(0.661, 0.492)
    d.click(0.441, 0.424)
    d.click(0.415, 0.419)
    d(resourceId="com.shinnytech.futures.kuaiqixiaoq.release:id/mdtp_ok").click()
# make sure next time will smooth
    ###screenshot
  #  d.swipe(0.461, 0.018, 0.397, 0.576)
   # d.click(0.68, 0.13)
    
   # d.app_stop("com.shinnytech.futures.kuaiqixiaoq.release")


