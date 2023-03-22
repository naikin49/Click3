#include <math.h>
#include <stdio.h>

struct borders
{
	int x1;
	int y1;
	int x2;
	int y2;
};

bool Is_Color_Eq(int distance, int r1, int g1, int b1, int r2, int g2, int b2)
{
	if (r1 == r2 && g1 == g2 && b1 == b2)
		return true;
	else
		return false;
	if (sqrt((r1 - r2) * (r1 - r2) + (g1 - g2) * (g1 - g2) + (b1 - b2) * (b1 - b2)) <= distance)
		return true;
	else
		return false;
}

int Is_img_eq(int* img1, int* img2, borders b1, borders b2, borders sb1, borders sb2)
{
	int sum = 0;
	for (int i = 0; i < sb1.x2 - sb1.x1; i++)
	{
		for (int j = 0; j < sb1.y2 - sb1.y1; j++)
		{
			int* one = &img1[((sb1.y1 + j) * b1.x2 + sb1.x1 + i) * 3];
			int* two = &img2[((sb2.y1 + j) * b2.x2 + sb2.x1 + i) * 3];
			if (Is_Color_Eq(6, one[0], one[1], one[2], two[0], two[1], two[2]))
				sum += 1;
		}
	}

	return int(float(sum) / float((sb1.x2 - sb1.x1) * (sb1.y2 - sb1.y1)) * 100);
}

int Is_img_similar(int* img1, int* img2, borders b1, borders b2, borders sb1, borders sb2, int pixel_num)
{
	int sum = 0;
	int x_step = (sb1.x2 - sb1.x1) / (pixel_num + 1);
	int y_step = (sb1.y2 - sb1.y1) / (pixel_num + 1);
	for (int i = x_step; i < sb1.x2 - sb1.x1; i = i + x_step)
	{
		for (int j = y_step; j < sb1.y2 - sb1.y1; j = j + y_step)
		{
			int* one = &img1[((sb1.y1 + j) * b1.x2 + sb1.x1 + i) * 3];
			int* two = &img2[((sb2.y1 + j) * b2.x2 + sb2.x1 + i) * 3];
			if (Is_Color_Eq(6, one[0], one[1], one[2], two[0], two[1], two[2]))
				sum += 1;
		}
	}

	return int(float(sum) / float(pixel_num * pixel_num) * 100);
}

#define DLL_EXPORT __declspec(dllexport) 
extern "C"  DLL_EXPORT void Find_Img(int acc, int* img1, int* img2, int x1, int y1, int x2, int y2, int* ans_x, int* ans_y)
{
	int max_acc = 0;
	int x = -1;
	int y = -1;
	for (int i = 0; i <= x1 - x2; i++)
	{
		for (int j = 0; j <= y1 - y2; j++)
		{
			borders b1 = { 0,0,x1,y1 };
			borders b2 = { 0,0,x2,y2 };
			borders sb1 = { i,j,i + x2,j + y2 };
			borders sb2 = { 0,0,x2,y2 };
			int new_acc = 0;
			if (Is_img_similar(img1, img2, b1, b2, sb1, sb2, 7) >= acc)
				new_acc = Is_img_eq(img1, img2, b1, b2, sb1, sb2);

			if (new_acc > max_acc)
			{
				max_acc = new_acc;
				x = i + x2 / 2;
				y = j + y2 / 2;
			}
		}
	}
	if (max_acc >= acc)
	{
		*ans_x = x;
		*ans_y = y;
	}
	else
	{
		*ans_x = -1;
		*ans_y = -1;
	}

}


