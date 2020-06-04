import numpy as np   # regular CLT program. hongik-jaewon, yongsang.

# in case orthotropic
      # isotropic E1x=E1y E2x=E2y E3x=E3y
      # anisotropic E1x,E1y incorrect values.

E1 =  list (map(float, input('enter the E1-1,E1-2,E1-3,E1-4:').split()))   # each lamina properties ex) E1-n  n :floor
E2 =  list (map(float, input('enter the E2-1,E2-2,E2-3,E2-4:').split()))   # each lamina properties ex) E2-n  n :floor
v12 = list (map(float, input('enter the v12-1,v12-2,v12-3,v12-4:').split()))  # each lamina properties ex) v12-n  n :floor
G12 = list (map(float,input('enter the G12-1,G12-2,G12-3,G12-4:').split()))   # each lamina properties ex) g12-n  n :floor


theta1, theta2,theta3,theta4 = list (map(float, input('enter the theta1-1, theta2-1, theta3-1,theta4-1:').split()))
 # each lamina properties ex) v12-n  n :floor
layup = np.array([theta1, theta2, theta3,theta4])

t = list (map(float,input('enter the t1, t2, t3, t4:').split()))    # height from mid-plane
h=sum(t)
print(h)
z = [x * h / len(E1) - h / 2 for x in range(len(E1))]
z.append(h / 2)
print(z)



Q= [ ]
for i in range(layup.shape[0]) :
    theta = layup[i] * np.pi / 180
    E111 = E1[i]
    E211 = E2[i]
    v121 = v12[i]
    G121 = G12[i]
    print('Ply no. ' + str(i + 1) + ': theta=' + str(layup[i]) + ', E111=' + str(E111), ' E211=' + str(E211))

    Q1 =  np.array([[E111**2 / (E111 - v121**2*E211), v121*E111*E211 / (E111 - E211*v121**2), 0], \
                        [v121*E111*E211 / (E111 - E211*v121**2), E111*E211 / (E111 -v121**2*E211), 0], \
                                           [0, 0, G121 ]])
    T = np.array([[np.cos(theta) ** 2, np.sin(theta) ** 2, -2 * np.sin(theta) * np.cos(theta)], \
                  [np.sin(theta) ** 2, np.cos(theta) ** 2, 2 * np.sin(theta) * np.cos(theta)], \
                  [np.sin(theta) * np.cos(theta), -np.sin(theta) * np.cos(theta),
                   np.cos(theta) ** 2 - np.sin(theta) ** 2]])
    Q.append(np.dot(np.dot(T, Q1), np.transpose(T)))
    print(Q[i])



A=np.zeros((3,3))
B=np.zeros((3,3))
D=np.zeros((3,3))

for i in  range(layup.shape[0]):
        A = A + Q[i] * (z[i+1] - z[i])
        B = B + Q[i] * (z[i+1] ** 2 - z[i] ** 2) / 2
        D = D + Q[i] * (z[i+1] ** 3 - z[i] ** 3) / 3




print('A matrix')
print(A)
print('B matrix')
print(B)
print('D matrix')
print(D)



ABD= np.vstack((np.hstack((A,B)),np.hstack((B,D))))
abd=np.linalg.inv(ABD)
print(ABD)
print(abd)

nx=float(1)
ny=1
float(ny)
nxy=1
float(nxy)
mx=1
float(mx)
my=1
float(my)
mxy=1
float(mxy)
print(nx, ny)
loadVector=np.array([[nx],[ny],[nxy],[mx],[my],[mxy]])
print(loadVector)
midplaneVector = abd.dot(loadVector)
print(midplaneVector)
midplaneStrains = midplaneVector[0:3, 0]  # top half
curvature = midplaneVector[3:6, 0]  # bottom half

print('midplaneStrains')
print(midplaneStrains)
print('curvature')
print(curvature)

#추가적인부분
Qstar = A/sum(t)                    # Qstar=A/t(tot)
Sstar = np.linalg.inv(Qstar)        # Sstar=(Qstar) 역함수
Ex = 1/Sstar[0,0]
Ey = 1/Sstar[1,1]
Gxy = 1/Sstar[2,2]
vxy=-Sstar[1,0]/Sstar[0,0]

print('Q* Matrix')
print(Qstar)
print('S* Matrix')
print(Sstar)

print('The total stiffness of the laminate is Ex='+ str(Ex)+
      ' and Ey=' + str(Ey) + ', with a shear modulus Gxy='+ str(Gxy) +
      ' and a poissons ratio of vxy='+str(vxy))

