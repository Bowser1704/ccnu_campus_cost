var cost_most=echarts.init(document.getElementById('cost_most'));
option = {
    backgroundColor:'#90ee90',
    dataset: {
        source: [
            ['score', 'amount', 'product'],
            [10, 14657.6, '2018210023'],
            [9, 11566.7, '2016211535'],
            [8, 10666.2, '2017215774'],
            [7, 10630.3, '2018211808'],
            [6, 10567.2, '2018214219'],
            [5, 10341.5, '2018213592'],
            [4, 10213.7, '2016212498'],
            [3, 10109.1, '2017215316'],
            [2, 9959.9, '2018212423'],
            [1, 9932.6, '2016213435']
        ]
    },
    grid: {containLabel: true},
    xAxis: {name: '消费总金额'},
    yAxis: {type: 'category',name:'学号'},
    visualMap: {
        orient: 'horizontal',
        left: 'center',
        min: 1,
        max: 10,
        text: ['High Score', 'Low Score'],
        // Map the score column to color
        dimension: 0,
        inRange: {
            color: [ '#E15457','#D7DA8B']
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
cost_most.setOption(option);