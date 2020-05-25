var ec_left1=echarts.init(document.getElementById('l1'),"dark");
var ec_left1_Option={
	title:{
		text:"学生2016210001的消费数据",
		textStyle:{
			
		},
		left:'left',
	},
	tooltip:{
		trigger:'axis',
		axisPointer:{
			type:'line',
			lineStyle:{
				color:'#7171c6'
			}
		},
	},
	legend:{
		data:['cost'],
		left:"right"
	},
	grid: {
	        left: '4%',
	        right: '6%',
	        bottom: '4%',
			top:50,
	        containLabel: true
	    },
	    
	    xAxis: [{
	        type: 'category',
	        data:[]// ['01.20', '01.21', '01.22']
	    }],
	    yAxis: [{
	        type: 'value',
			axisLabel:{
				show:true,
				color:'white',
				fontSize:12,
				formatter:function(value){
					if(value>=1000){
						value=value/1000+'k';
					}
					return value;
				}
			},
			axisLine:{
				show:true
			},
			splitLine:{
				show:true,
				lineStyle:{
					color:'#17273b',
					width:1,
					type:'solid',
				}
			}
	    }],
	series:[{
		name:'cost',
		type:'line',
		smooth:true,
		data:[]//[260,406,529]
	}]

	
};
ec_left1.setOption(ec_left1_Option)