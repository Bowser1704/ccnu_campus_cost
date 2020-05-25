function get_l1_data(){
    $.ajax({
        url:"/l1",
        success:function(data){
					ec_left1_Option.xAxis[0].data=data.day
			        ec_left1_Option.series[0].data=data.cost
					ec_left1.setOption(ec_left1_Option)
				},
				error:function(xhr,type,errorThrown){

				}

            });
}
function get_l2_data(){
    $.ajax({
        url:"/l2",
        success:function(data){
					ec_left2_Option.xAxis[0].data=data.day
			        ec_left2_Option.series[0].data=data.cost
					ec_left2.setOption(ec_left2_Option)
				},
				error:function(xhr,type,errorThrown){

				}

            });
}
function get_r1_data(){
    $.ajax({
        url:"/r1",
        success:function(data){
					ec_right1_Option.xAxis[0].data=data.day
			        ec_right1_Option.series[0].data=data.cost
					ec_right1.setOption(ec_right1_Option)
				},
				error:function(xhr,type,errorThrown){

				}

            });
}
function get_r2_data(){
    $.ajax({
        url:"/r2",
        success:function(data){
					ec_right2_Option.xAxis[0].data=data.day
			        ec_right2_Option.series[0].data=data.cost
					ec_right2.setOption(ec_right2_Option)
				},
				error:function(xhr,type,errorThrown){

				}

            });
}
get_l1_data()
get_l2_data()
get_r1_data()
get_r2_data()