from pyecharts import Pie


def get_html():
    # encoding:utf-8
    '''
    add(name,attr,value,radius = None,center = None,rosetype = None,**kwargs)
    attr:属性名称
    radius：饼图半径，数组第一项是内径，第二项是外径，默认[0,75,],设置成百分比
    center：圆心，数组第一项是X轴，第二项是Y轴，默认[50,50]
    rosetype: 是否展示成南丁格尔图，用过半径区分数据大小，radius和area两种模式，默认radius'''
    
    
    pie1 = Pie('')  # 创建实例
  

    attr = []   #餐厅
    value1 = []   #次数

    pie1.add('', attr, value1, is_label_show=True)
    

    '''
    如果需要横向并列图 可在最后的add括号中添加 (---snip---,is_convert = True) 表示X 轴与 Y 轴交换
    '''
    pie1.show_config()  # 调试输出pyecharts的js配置信息
  
    pie1.render('饼图.html')
    





if __name__ == "__main__":
    get_html()

