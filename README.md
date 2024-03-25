# Photo to Cartoon
> ## Using OpenCV to Create Cartoons from Videos


## 카툰 느낌이 잘 표현되는 영상의 스크린 샷


![image](https://github.com/SJ-1011/Photo_to_Cartoon/assets/109647265/274f533d-0157-4710-b18e-12b7fb359e47)



카툰 느낌이 적당하게 표현 됨을 볼 수 있다.






## 카툰 느낌이 잘 표현되지 않는 영상의 스크린 샷


![image](https://github.com/SJ-1011/Photo_to_Cartoon/assets/109647265/d002743a-5813-473b-8543-96c285df8c9e)


임계 상수 C를 음수를 하였더니 반전이 되었다.


카툰 느낌은 더 잘 표현됐을수도 있지만, 원본의 느낌을 많이 잃어 잘 표현되었다고 할 수 없다.




## 알고리즘의 한계

1. 해당 알고리즘은 특정 이미지/비디오에 대해서만 효과적 일 수 있다. 아래는 고양이 사진을 카툰화한 것인데, 고양이 사진이 새 사진보다 카툰화가 비교적 깔끔하게 잘 된 것을 확인할 수 있다.


![cartoon_cat2](https://github.com/SJ-1011/Photo_to_Cartoon/assets/109647265/6ed821c4-287c-4451-930b-a84d9fe0ee2f)


2. 해당 알고리즘은 블러 효과도 있기 때문에 이미지의 세부 정보가 손실 될 수 있다.


3. 해당 알고리즘으로 카툰화를 하면 비디오의 용량이 커져 계산 비용이 커진다는 한계가 있다.
