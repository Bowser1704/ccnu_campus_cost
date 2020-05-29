var costumeCount=echarts.init(document.getElementById('costumeCount'));
option = {

    dataset: {
        source: [
            ['score', 'amount', 'product'],
            [10, 396724, '学子超市/超市'],
            [9, 326409, '学子餐厅/吧台左'],
            [8, 315917, '东一餐厅/稀食'],
            [7, 310467, '东一餐厅/休闲食品'],
            [6, 224974, '桂香园餐厅/豆浆'],
            [5, 202859, '学子中西餐厅/一楼'],
            [4, 184473, '东一餐厅/大白案'],
            [3, 181953, '学子餐厅/精品套餐'],
            [2, 176561, '东一餐厅/煎饼'],
            [1, 174840, '学子餐厅/吧台右']
        ]
    },
    title:{
        show:'true',
        text:'窗口消费次数排行榜',
        left:'50%'
    },
    grid: {containLabel: true},
    xAxis: {name: '刷卡次数'},
    yAxis: {type: 'category',name:'窗口'},
    visualMap: {
        show:'false',
        orient: 'horizontal',
        left: 'center',
        min: 1,
        max: 10,
        text: ['High Score', 'Low Score'],
        // Map the score column to color
        dimension: 0,
        inRange: {
            color: [ '#23cbff','#2f83e4']
        }
    },
    series: [
        {
            type: 'bar',
            encode: {
                // Map the "amount" column to X axis.
                x: 'amount',
                // Map the "product" column to Y axis
                y: 'product'
            }
        }
    ]
};
costumeCount.setOption(option);