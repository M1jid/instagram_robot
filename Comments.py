class Comments:
    '''
    NAME
        Comments
    =============================
    
    Description :
        this class return random comment
        
    ================
    input : list of comments
    
    ==============================
    output : random comment
    
    '''
    def comments():
        import random
        comments_list = ['😍عالیه', '🔥چه عالی', 'خیلی جذابه', 'چقدرنازه', 'محشره😍', 'چه خوبه', 'خیلی خوشم اومد', 'دوسش داشتم', 'چقدر طرحش نازه😍', 
                         'چقدر رنگش قشنگه😍', 'رنگش عالیه', 'مدلش عالیه' , '🔥پر فروش باشی عزیزم' , 'چقدر کیوته' , '🔥پر روزی باشی گلم' ,'چقدر شیکه' ,
                         'خیلی شیکه😍']
        for commen in range(len(comments_list)):
            com = random.randint(1,len(comments_list)-1)
            comment = comments_list[com]

        return comment