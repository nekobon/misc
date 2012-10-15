% A matlab file to generate a 3D animation of a unit vector rotating
% in a meshed sphere.
%
% Yu Tomita
% (yu.t@gatech.edu)
% 2009

% --To save as .avi, do:
% >> movie2avi(A,"fileName.avi")
% 
% --To convert .avi->.gif, we can do:
% $ mplayer fileName.avi -vo gif89a:output=gifFile.gif:fps=10
% on linux command. fps can be any nuber. Requires mplayer.

figure(1)
set(0,'DefaultLineLineWidth',3,'DefaultLineColor','black','DefaultLineMarkerSize',
10,'DefaultAxesLineWidth',2,'DefaultAxesFontName','Helvetica','DefaultAxesFontSize',
25,'DefaultTextFontName','Helvetica','DefaultTextFontSize',25,'DefaultSurfaceFaceLighting',
'phong')
numframes=70;               % number of frames of animation
A=moviein(numframes);       % initialize empty frames

% display settings
set(gcf,'menubar','none')
set(gcf,'numbertitle','off') 
set(gcf, 'color','white')      
set(gca,'DataAspectRatio',[1 1 3], 'PlotBoxAspectRatio',[1 1 1],'ZLim',[-5 5], 'YLim', 
[-5 5], 'XLim', [-5 5]); %ratio, etc..

% main part starts here
angle=0;
[X,Y,Z]=sphere(30);            
p=mesh(X,Y,Z,'EdgeColor','black');           
alpha('clear');
hold on

% set up axes
D=linspace(0,1,90);
B=D;
C=B;
plot3(0*D,0*B,C,'-k',0*D,0*B,-C,'-k',0*D,B,0*C,'-k',0*D,-B,0*C,'-k',D,0*B,0*C,'-k',-D,0*B,0*C,'-k');
h = plot3(0*D,0*B,C,'-r'); % contains main vector
text(0,-1.5,0,'-y');
text(1.3,0,0,'x');
text(0,.2,1.4,'|0\rangle')
text(0,.2,-1.4,'|1\rangle')
axis([-1 1 -1 1 -1 1])
axis off
grid off
angle=0;

% MAIN LOOP
% Simulates applying a pi/2 pulse bring the state to 1/sqrt(2)(|0>+|1>)
% (Rotate a vector for 90 degrees)
for i=1:19
    rotate(h,[1 0 0],angle)   % rotate object h in x direction 
    A(:,i)=getframe;
    angle=10;% save frame in A
    pause(1) % without this, image is destroyed before saving by going next loop-step too far
end
% save as a movie
movie2avi(A,'idealvsnonideal.avi')
