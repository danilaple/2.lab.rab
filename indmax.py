int main()
{
    double alp,m1,min_h,step;
    int hour,minutes=0;
 
    scanf("%lf",&alp); //ввод угла от 0 до 2*PI
 
    hour=alp/(2*PI/12); // целых часов
    m1=2*PI/60;         // угол одной минуты для минутной стрелки
    step=(2*PI/12)/60;   // угол одной минуты в пределах часа, для часовой стрелки
    min_h=(2*PI/12)*hour; // угол целого часа
 
    while(min_h<alp)  // пока угол не достигнет введенного значения
    {
        min_h+=step;  // улол увеличиваем
        minutes++;   //  считаем минуты
    }
 
    if(minutes==60)  // если введено пограничное значение
    {
        minutes=0;  //  обнуляем минуты
        hour++;    //  увеличиваем часы
    }
 
    printf("Hour = %d\n",hour);
    printf("Minutes = %d\n",minutes);
    printf("Min len = %lf\n",minutes*m1);
 
    return 0;
}
