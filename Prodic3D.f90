!     Last change:  UU   13 Jul 1994    5:06 am
!||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
           PROGRAM PRODIC3D
!          NUEVA VERSION DEL PROGRAMA 'PRODIC'
!                   REALIZADO POR RODRIGUEZ M. MARCEL L.
!           UNIVERSIDAD DEL ZULIA. ESCUELA DE INGENIERIA MECANICA
!                 LABORATORIO DE SIMULACION COMPUTACIONAL
!                        TUTOR: PHD ING. JUAN DAMIA
!______________________________________________________________________
      INCLUDE '3DCOMMON.F90'
      CHARACTER*8 PLOTN
!______________________________________________________________________
!     CALCULOS EN LA FASE INICIAL
      CALL DEFLT
      CALL GRID
      CALL READY
      CALL BEGIN
!     COMIENZO DE LA MARCHA EN EL TIEMPO
      PLOTN=PLOTF
      DO NPTI=0,IPTM
       KEPR=0
       KEPL=0
       KPGR=1
!        COLECCION DE LOS VALORES VECINOS EN EL TIEMPO
       DO K=1,N1
        DO I=1,L1
	 DO J=1,M1
	  DO NF=1,NFMAX
	   FOLD(I,J,K,NF)=F(I,J,K,NF)
          END DO
         END DO
        END DO
       END DO
!OMIENZO DEL LAZO DE ITERACIONES
	 DO ITER=0,LAST
	  CALL DENSE
	  CALL BOUND
          CALL OUTPUT
!REA UN CRITERIO ADICIONAL DE CONVERGENCIA
          IF((SMAX.LE.TOL.AND.ITER.GT.3).OR.(ITER.EQ.LAST.AND.LAST.GT.0).OR.KSTOP.EQ.1) GO TO 10
	  CALL HEART1
	  CALL COPRES
	  CALL HEART2
	 END DO
!AMINA AL SIGUIENTE INTERVALO DE TIEMPO
   10    CONTINUE
         TIME=TIME+DT
         CALL PRINT
!REA METODO PARA GENERAR LA EXTENSION DE ARCHIVOS PARA TECPLOT
         IF(KEPL.EQ.0) THEN
           NNN1= NPTI/100
           NNN2=(NPTI-NNN1*100)/10
           NNN3=NPTI-NNN1*100-NNN2*10
           IF(NNN1.GT.9) NNN1=0
           PLOTF=PLOTN//CHAR(46)//CHAR(nnn1+48)//&
     &           char(nnn2+48)//char(nnn3+48)
           CALL PLOT
         ENDIF
      END DO
      END
!>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
      SUBROUTINE SETUP
!<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
      INCLUDE '3DCOMMON.F90'
!     =================================================================
      ENTRY DEFLT
!     ����������?
!     ASIGNA VALORES POR DEFECTO
      HEADER='USE HEADER PARA ESPECIFICAR EL TITULO DEL PROBLEMA'
      PRINTF='PRINT1'
      PLOTF='PLOT1'
      KCY=0; KSTOP=0; LAST=25; ITER=0; KORD=2; MODE=1; KOUT=3; KPGR=1
      SMALL=1.E-20; BIG=1.E+20; TIME=0.; DT=1.E+20; R(1)=0.;  IPTM=0
      POWERX=1.; POWERY=1.; POWERZ=1.; SMAX=1.E-4; TOL=1.E-5
      IBORX=0; IBORY=0; IBORZ=0; IPUN=0
      DO NZ=1,NZMAX
       POWRX(NZ)=1.
       POWRY(NZ)=1.
       POWRZ(NZ)=1.
      ENDDO
      DO N=1,NFMAX
       CRIT(N)=1.E-5
       KSOLVE(N)=0
       NTIMES(N)=10
       KBLOC(N)=1
       IBORX(N)=0; IBORY(N)=0; IBORZ(N)=0; IPUN(N)=0
       DO J=2,NJ
        DO I=2,NI
         FLUXK1(I,J,N)=0.
         FLUXN1(I,J,N)=0.
        ENDDO
       ENDDO
       DO K=2,NK
        DO I=2,NI
         FLUXJ1(I,K,N)=0.
         FLUXM1(I,K,N)=0.
        ENDDO
       ENDDO
       DO K=2,NK
        DO J=2,NJ
         FLUXI1(J,K,N)=0.
         FLUXL1(J,K,N)=0.
        ENDDO
       ENDDO
      ENDDO
      DO N=1,NP
       RELAX(N)=1.
       WRITE(TITLE(N),'(I2)')N
       KPRINT(N)=0
       IXYZ(N)=3
      ENDDO
      DO K=1,NK
       DO J=1,NJ
        DO I=1,NI
         P(I,J,K)=0.
         CON(I,J,K)=0.
         AP(I,J,K)=0.
         RHO(I,J,K)=1.
         GAM(I,J,K)=1.
         IBLOCK(I,J,K)=0
         DO N=1,NFMAX
          F(I,J,K,N)=0.
         ENDDO
        ENDDO
       ENDDO
      ENDDO
      DO J=2,NJ
       DO I=2,NI
        KBCK1(I,J)=1
        KBCN1(I,J)=1
        FLXCK1(I,J)=0.
        FLXCN1(I,J)=0.
        FLXPK1(I,J)=0.
        FLXPN1(I,J)=0.
       ENDDO
      ENDDO
      DO K=2,NK
       DO I=2,NI
        KBCJ1(I,K)=1
        KBCM1(I,K)=1
        FLXCJ1(I,K)=0.
        FLXCM1(I,K)=0.
        FLXPJ1(I,K)=0.
        FLXPM1(I,K)=0.
       ENDDO
      ENDDO
      DO K=2,NK
       DO J=2,NJ
        KBCI1(J,K)=1
        KBCL1(J,K)=1
        FLXCI1(J,K)=0.
        FLXCL1(J,K)=0.
        FLXPI1(J,K)=0.
        FLXPL1(J,K)=0.
       ENDDO
      ENDDO
      RETURN
!     =================================================================
      ENTRY READY
!     ����������?
      IF(KOUT.NE.1) OPEN(UNIT=7,FILE=PRINTF)
      IU1=6
      IF(KOUT.EQ.2) IU1=7
      IU2=7
      IF(KOUT.EQ.1) IU2=6
!     GENERACION DE LA SALIDA INICIAL
      DO IUNIT=IU1,IU2
      IF(MODE.EQ.1) WRITE(IUNIT,1)
    1 FORMAT(1X,'RESULTADOS DEL PRODIC3D PARA UN SISTEMA DE COORDENADAS&
     &CARTESIANAS'/1X,65(1H*)//)
      IF(MODE.EQ.2) WRITE(IUNIT,3)
    3 FORMAT(1X,'RESULTADOS DEL PRODIC3D PARA UN SISTEMA DE COORDENADAS&
     &CILINDRICAS'/1X,65(1H*)//)
      WRITE(IUNIT,6) HEADER
    6 FORMAT(1X,72('-')/1X,A64/1X,72('-')//)
      IF(L1.GT.NI.OR.M1.GT.NJ.OR.N1.GT.NK.OR.(L1.LT.4).OR.&
     &   M1.LT.4.OR.(N1.LT.4))&
     &   THEN
      WRITE(IUNIT,7)
    7 FORMAT(1X,'EJECUCION TERMINADA DEBIDO A UNA (O MAS) DE LAS SIGUIEN&
     &TES RAZONES:'/2X,'1) L1 MAYOR QUE NI'/2X,'2) M1 MAYOR QUE NJ'&
     &/2X,'3) N1 MAYOR QUE NK'/2X,'4) L1 MENOR QUE 4'&
     &/2X,'5) M1 MENOR QUE 4'/2X,'6) N1 MENOR QUE 4'&
     &/2X)
      KSTOP=1
      ENDIF
      ENDDO
      IF(KSTOP.NE.0) STOP
!     CALCULA CANTIDADES GEOMETRICAS
      L2=L1-1
      L3=L2-1
      M2=M1-1
      M3=M2-1
      N2=N1-1
      N3=N2-1

      X(1)=XU(2)
!     UBICACION DE NODOS DIR. 'X'
      DO I=2,L2
         X(I)=0.5*(XU(I+1)+XU(I))
      ENDDO
      X(L1)=XU(L1)
!     DISTANCIA ENTRE NODOS DIR. 'X' (INCLUYENDO NODOS EN EL BORDE)
      DO I=2,L1
         XDIF(I)=X(I)-X(I-1)
      ENDDO
!     ANCHO DE CELDA EN DIR. 'X'
      DO I=2,L2
         XCV(I)=XU(I+1)-XU(I)
      ENDDO
!     ANCHO DE CELDA PARA VELOCIDADES
      DO I=3,L2
         XCVS(I)=XDIF(I)
      ENDDO
      XCVS(3)=XCVS(3)+XDIF(2)
      XCVS(L2)=XCVS(L2)+XDIF(L1)
!     ANCHOS DE CELDA NO DESPLAZADA SOLAPADAS SOBRE
!     MALLA DESPLAZADA EN LA DIRECCI? "X"
      DO I=3,L3
         XCVI(I)=0.5*XCV(I)
         XCVIP(I)=XCVI(I)
      ENDDO
      XCVIP(2)=XCV(2)
      XCVI(L2)=XCV(L2)

      Y(1)=YV(2)
!     UBICACION DE NODOS DIR. 'Y'
      DO J=2,M2
         Y(J)=0.5*(YV(J+1)+YV(J))
      ENDDO
      Y(M1)=YV(M1)
!     DISTANCIA ENTRE NODOS DIR. 'Y' (INCLUYENDO NODOS EN EL BORDE)
      DO J=2,M1
         YDIF(J)=Y(J)-Y(J-1)
      ENDDO
!     ANCHO DE CELDA EN DIR. 'Y'
      DO J=2,M2
         YCV(J)=YV(J+1)-YV(J)
      ENDDO
!     ANCHO DE CELDA PARA VELOCIDADES
      DO J=3,M2
         YCVS(J)=YDIF(J)
      ENDDO
      YCVS(3)=YCVS(3)+YDIF(2)
      YCVS(M2)=YCVS(M2)+YDIF(M1)
!     DEFINICION DE RADIOS SEGUN AL SISTEMA COORDENADO (MODE)
       IF(MODE.EQ.1) THEN
        DO J=1,M1
           RV(J)=1.
           R(J)=1.
        ENDDO
       ELSE
        DO J=2,M1
           R(J)=R(J-1)+YDIF(J)
        ENDDO
         RV(2)=R(1)
         DO J=3,M2
            RV(J)=RV(J-1)+YCV(J-1)
         ENDDO
         RV(M1)=R(M1)
       ENDIF
!
       IF(MODE.EQ.1) THEN
        DO J=1,M1
           SX(J)=1.
           SXMN(J)=1.
        ENDDO
       ELSE
        DO J=1,M1
           SX(J)=R(J)
           IF(J.NE.1) SXMN(J)=RV(J)
        ENDDO
      ENDIF
!
      DO J=2,M2
         YCVR(J)=R(J)*YCV(J)
      ENDDO
!
      DO J=4,M3
         YCVRS(J)=0.5*(R(J)+R(J-1))*YDIF(J)
      ENDDO
         YCVRS(3)=0.5*(R(3)+R(1))*YCVS(3)
         YCVRS(M2)=0.5*(R(M1)+R(M3))*YCVS(M2)
!     ANCHOS DE CELDA NO DESPLAZADA SOLAPADAS SOBRE
!     MALLA DESPLAZADA EN LA DIRECCI? "X"
      IF(MODE.EQ.2) THEN
        DO J=3,M3
           YCVJ(J)=0.25*(1.+RV(J)/R(J))*YCVR(J)
           YCVJP(J)=YCVR(J)-YCVJ(J)
        ENDDO
        YCVJP(2)=YCVR(2)
        YCVJ(M2)=YCVR(M2)
        ELSE
        DO J=3,M3
           YCVJ(J)=0.5*YCV(J)
           YCVJP(J)=YCVJ(J)
        ENDDO
        YCVJP(2)=YCV(2)
        YCVJ(M2)=YCV(M2)
      ENDIF
!
      DO J=3,M3
         YCDJ(J)=0.5*YCV(J)
         YCDJP(J)=YCDJ(J)
      ENDDO
      YCDJP(2)=YCV(2)
      YCDJ(M2)=YCV(M2)
!
      DO J=3,M3
         FV(J)=YCVJP(J)/YCVR(J)
         FVP(J)=1.-FV(J)
      ENDDO
!
      Z(1)=ZW(2)
!     UBICACION DE NODOS DIR. 'Z'
      DO K=2,N2
         Z(K)=0.5*(ZW(K+1)+ZW(K))
      ENDDO
      Z(N1)=ZW(N1)
!     DISTANCIA ENTRE NODOS DIR. 'Z' (INCLUYENDO NODOS EN EL BORDE)
      DO K=2,N1
         ZDIF(K)=Z(K)-Z(K-1)
      ENDDO
!     ANCHO DE CELDA EN DIR. 'Z'
      DO K=2,N2
         ZCV(K)=ZW(K+1)-ZW(K)
      ENDDO
!     ANCHO DE CELDA PARA VELOCIDADES
      DO K=3,N2
         ZCVS(K)=ZDIF(K)
      ENDDO
      ZCVS(3)=ZCVS(3)+ZDIF(2)
      ZCVS(N2)=ZCVS(N2)+ZDIF(N1)
!     ANCHOS DE CELDA NO DESPLAZADA SOLAPADAS SOBRE
!     MALLA DESPLAZADA EN LA DIRECCI? "X"
      DO K=3,N3
         ZCVK(K)=0.5*ZCV(K)
         ZCVKP(K)=ZCVK(K)
      ENDDO
      ZCVKP(2)=ZCV(2)
      ZCVK(N2)=ZCV(N2)
!     AREA PERPENDICULAR A LA DIRECCI? 'X'
      DO K=2,N2
        DO J=2,M2
           ARX(J,K)=YCV(J)*ZCV(K)
         ENDDO
      ENDDO
!     AREA PERPENDICULAR A LA DIRECCI? 'Z'
      DO J=2,M2
        DO I=2,L2
           ARZ(I,J)=XCV(I)*YCVR(J)
        ENDDO
      ENDDO
!     FACTORES DE INTERPOLACI? EN DIRECCI? 'X'
      DO I=3,L2
         FX(I)=0.5*XCV(I-1)/XDIF(I)
         FXM(I)=1.-FX(I)
      ENDDO
      FX(2)=0.
      FXM(2)=1.
      FX(L1)=1.
      FXM(L1)=0.
!     FACTORES DE INTERPOLACI? EN DIRECCI? 'Y'
      DO J=3,M2
         FY(J)=0.5*YCV(J-1)/YDIF(J)
         FYM(J)=1.-FY(J)
      ENDDO
      FY(2)=0.
      FYM(2)=1.
      FY(M1)=1.
      FYM(M1)=0.
!     FACTORES DE INTERPOLACI? EN DIRECCI? 'Z'
      DO K=3,N2
         FZ(K)=0.5*ZCV(K-1)/ZDIF(K)
         FZM(K)=1.-FZ(K)
      ENDDO
      FZ(2)=0.
      FZM(2)=1.
      FZ(N1)=1.
      FZM(N1)=0.
      RETURN
      END
!>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
      SUBROUTINE HEART1
!<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
      INCLUDE '3DCOMMON.F90'
!     =================================================================
!----------------------------------------------------------------------
!     COEFICIENTES PARA LA ECUACION DE LA COMPONENTE DE VELOCIDAD "U"
!----------------------------------------------------------------------
      NF=1
      IF(KSOLVE(NF).EQ.0) GO TO 20
      IST=3                                                             
      JST=2                                                            
      KST=2                                                            
      CALL PHI
      RLX=(1.-RELAX(NF))/RELAX(NF)
!ONSIDERACION DE LOS TERMINOS VOLUMETRICOS
      DO K=2,N2
       DO J=2,M2
        DO I=3,L2
         VOL=ZCV(K)*YCVR(J)*XCVS(I)
         APT=(RHO(I,J,K)*XCVI(I)+RHO(I-1,J,K)*XCVIP(I-1))/(XCVS(I)*DT)
         AP(I,J,K)=(APT-AP(I,J,K))*VOL
         CON(I,J,K)=(CON(I,J,K)+APT*FOLD(I,J,K,NF))*VOL
        ENDDO
       ENDDO
      ENDDO
!ALCULO DE LOS COEFICIENTES EN LA DIRECCION X
      LEND=L3
      IF(KCY.NE.0) LEND=L2
      DO K=2,N2
       DO J=2,M2
        DO I=3,LEND
         IFOR=I+1
         IF(I.EQ.L2) IFOR=IST
         FL=F(I,J,K,1)*(FX(I)*RHO(I,J,K)+FXM(I)*RHO(I-1,J,K))
         FLP=F(IFOR,J,K,1)*(FX(IFOR)*RHO(IFOR,J,K)+FXM(IFOR)*RHO(I,J,K))
         FLOW=ARX(J,K)*0.5*(FL+FLP)
         DIFF=ARX(J,K)*GAM(I,J,K)/(XCV(I)*SX(J))+SMALL
         CALL DIFLOW
              AIM(IFOR,J,K)=ACOF+MAX(FLOW,0.)
              AIP(I,J,K)=AIM(IFOR,J,K)-FLOW
        ENDDO
       ENDDO
      ENDDO
      IF(KCY.NE.0) GO TO 30
!ONSIDERA EL PLANO I=2 PARA LA VELOCIDAD "U". MALLA DESPLAZADA
      DO K=2,N2
       DO J=2,M2
        FLOW=F(2,J,K,1)*RHO(1,J,K)
        DIFF=GAM(1,J,K)/(XCV(2)*SX(J))+SMALL
        CALL DIFLOW
             AIM(3,J,K)=ACOF+MAX(FLOW,0.)
             AIP(2,J,K)=AIM(3,J,K)-FLOW
             AIM(3,J,K)=AIM(3,J,K)*ARX(J,K)
             AIM(2,J,K)=0.
        IF(KBCI1(J,K).EQ.1) THEN
          CON(3,J,K)=CON(3,J,K)+AIM(3,J,K)*F(2,J,K,NF)
        ELSE
          AP(2,J,K)=AIP(2,J,K)-FLXPI1(J,K)
          CON(2,J,K)=FLXCI1(J,K)
          TEMP=AIM(3,J,K)/AP(2,J,K)
          AP(3,J,K)=AP(3,J,K)-AIP(2,J,K)*TEMP
          CON(3,J,K)=CON(3,J,K)+CON(2,J,K)*TEMP
        ENDIF
        AP(3,J,K)=AP(3,J,K)+AIM(3,J,K)
        AIM(3,J,K)=0.
!ONSIDERA EL PLANO I=L1
        FLOW=F(L1,J,K,1)*RHO(L1,J,K)
        DIFF=GAM(L1,J,K)/(XCV(L2)*SX(J))+SMALL
        CALL DIFLOW
             AIP(L2,J,K)=ACOF+MAX(-FLOW,0.)
             AIM(L1,J,K)=AIP(L2,J,K)+FLOW
             AIP(L2,J,K)=AIP(L2,J,K)*ARX(J,K)
             AIP(L1,J,K)=0.
        IF(KBCL1(J,K).EQ.1) THEN
          CON(L2,J,K)=CON(L2,J,K)+AIP(L2,J,K)*F(L1,J,K,NF)
        ELSE
          AP(L1,J,K)=AIM(L1,J,K)-FLXPL1(J,K)
          CON(L1,J,K)=FLXCL1(J,K)
          TEMP=AIP(L2,J,K)/AP(L1,J,K)
          AP(L2,J,K)=AP(L2,J,K)-AIM(L1,J,K)*TEMP
          CON(L2,J,K)=CON(L2,J,K)+CON(L1,J,K)*TEMP
        ENDIF
        AP(L2,J,K)=AP(L2,J,K)+AIP(L2,J,K)
        AIP(L2,J,K)=0.
       ENDDO
      ENDDO
   30 CONTINUE
!ALCULO DE LOS COEFICIENTES EN LA DIRECCION Y
      DO K=2,N2
       DO J=2,M3
        DO I=3,L2
         AREA=ZCV(K)*RV(J+1)
         FL=XCVI(I)*F(I,J+1,K,2)*(FY(J+1)*RHO(I,J+1,K)&
     &     +FYM(J+1)*RHO(I,J,K))
         FLM=XCVIP(I-1)*F(I-1,J+1,K,2)*(FY(J+1)*RHO(I-1,J+1,K)&
     &     +FYM(J+1)*RHO(I-1,J,K))
         GM=GAM(I,J,K)*GAM(I,J+1,K)/(YCV(J)*GAM(I,J+1,K)&
     &     +YCV(J+1)*GAM(I,J,K)+SMALL)*XCVI(I)
         GMM=GAM(I-1,J,K)*GAM(I-1,J+1,K)/(YCV(J)*GAM(I-1,J+1,K)&
     &     +YCV(J+1)*GAM(I-1,J,K)+SMALL)*XCVIP(I-1)
         FLOW=AREA*(FL+FLM)
         DIFF=2.*AREA*(GM+GMM)
         CALL DIFLOW
              AJM(I,J+1,K)=ACOF+MAX(FLOW,0.)
              AJP(I,J,K)=AJM(I,J+1,K)-FLOW
        ENDDO
       ENDDO
      ENDDO
!ONSIDERA EL PLANO J=1
      DO K=2,N2
       DO I=3,L2
        XCVT=XCVI(I)+XCVIP(I-1)
        FL=XCVI(I)*F(I,2,K,2)*RHO(I,1,K)
        FLM=XCVIP(I-1)*F(I-1,2,K,2)*RHO(I-1,1,K)
        FLOW=(FL+FLM)/XCVT
        DIFF=(XCVI(I)*GAM(I,1,K)+XCVIP(I-1)*GAM(I-1,1,K))/&
     &       (YDIF(2)*XCVT)+SMALL
        CALL DIFLOW
             AJM(I,2,K)=ACOF+MAX(FLOW,0.)
             AJP(I,1,K)=AJM(I,2,K)-FLOW
             AJM(I,2,K)=AJM(I,2,K)*R(1)*XCVT*ZCV(K)
             AJM(I,1,K)=0.
        IF(KBCJ1(I,K).EQ.1) THEN
          CON(I,2,K)=CON(I,2,K)+AJM(I,2,K)*F(I,1,K,NF)
        ELSE
          AP(I,1,K)=AJP(I,1,K)-FLXPJ1(I,K)
          CON(I,1,K)=FLXCJ1(I,K)
          TEMP=AJM(I,2,K)/AP(I,1,K)
          AP(I,2,K)=AP(I,2,K)-AJP(I,1,K)*TEMP
          CON(I,2,K)=CON(I,2,K)+CON(I,1,K)*TEMP
        ENDIF
        AP(I,2,K)=AP(I,2,K)+AJM(I,2,K)
        AJM(I,2,K)=0.
!ONSIDERA EL PLANO J=M1
        FL=XCVI(I)*F(I,M1,K,2)*RHO(I,M1,K)
        FLM=XCVIP(I-1)*F(I-1,M1,K,2)*RHO(I-1,M1,K)
        FLOW=(FL+FLM)/XCVT
        DIFF=(XCVI(I)*GAM(I,M1,K)+XCVIP(I-1)*GAM(I-1,M1,K))/&
     &       (YDIF(M1)*XCVT)+SMALL
        CALL DIFLOW
             AJP(I,M2,K)=ACOF+MAX(-FLOW,0.)
             AJM(I,M1,K)=AJP(I,M2,K)+FLOW
             AJP(I,M2,K)=AJP(I,M2,K)*R(M1)*XCVT*ZCV(K)
             AJP(I,M1,K)=0.
        IF(KBCM1(I,K).EQ.1) THEN
          CON(I,M2,K)=CON(I,M2,K)+AJP(I,M2,K)*F(I,M1,K,NF)
        ELSE
          AP(I,M1,K)=AJM(I,M1,K)-FLXPM1(I,K)
          CON(I,M1,K)=FLXCM1(I,K)
          TEMP=AJP(I,M2,K)/AP(I,M1,K)
          AP(I,M2,K)=AP(I,M2,K)-AJM(I,M1,K)*TEMP
          CON(I,M2,K)=CON(I,M2,K)+CON(I,M1,K)*TEMP
        ENDIF
        AP(I,M2,K)=AP(I,M2,K)+AJP(I,M2,K)
        AJP(I,M2,K)=0.
       ENDDO
      ENDDO
!ALCULOS DE LOS COEFICIENTES EN LA DIRECCION Z
      DO K=2,N3
       DO J=2,M2
        DO I=3,L2
         FL=XCVI(I)*F(I,J,K+1,3)*(FZ(K+1)*RHO(I,J,K+1)&
     &     +FZM(K+1)*RHO(I,J,K))
         FLM=XCVIP(I-1)*F(I-1,J,K+1,3)*(FZ(K+1)*RHO(I-1,J,K+1)&
     &     +FZM(K+1)*RHO(I-1,J,K))
         GM=GAM(I,J,K)*GAM(I,J,K+1)/(ZCV(K)*GAM(I,J,K+1)&
     &     +ZCV(K+1)*GAM(I,J,K)+SMALL)*XCVI(I)
         GMM=GAM(I-1,J,K)*GAM(I-1,J,K+1)/(ZCV(K)*GAM(I-1,J,K+1)&
     &     +ZCV(K+1)*GAM(I-1,J,K)+SMALL)*XCVIP(I-1)
         FLOW=YCVR(J)*(FL+FLM)
         DIFF=2.*YCVR(J)*(GM+GMM)
         CALL DIFLOW
              AKM(I,J,K+1)=ACOF+MAX(FLOW,0.)
              AKP(I,J,K)=AKM(I,J,K+1)-FLOW
        ENDDO
       ENDDO
      ENDDO
!ONSIDERA EL PLANO K=1
      DO J=2,M2
       DO I=3,L2
        XCVT=XCVI(I)+XCVIP(I-1)
        FL=XCVI(I)*F(I,J,2,3)*RHO(I,J,1)
        FLM=XCVIP(I-1)*F(I-1,J,2,3)*RHO(I-1,J,1)
        FLOW=(FL+FLM)/XCVT
        DIFF=(XCVI(I)*GAM(I,J,1)+XCVIP(I-1)*GAM(I-1,J,1))/&
     &       (ZDIF(2)*XCVT)+SMALL
        CALL DIFLOW
             AKM(I,J,2)=ACOF+MAX(FLOW,0.)
             AKP(I,J,1)=AKM(I,J,2)-FLOW
             AKM(I,J,2)=AKM(I,J,2)*XCVT*YCVR(J)
             AKM(I,J,1)=0.
        IF(KBCK1(I,J).EQ.1) THEN
          CON(I,J,2)=CON(I,J,2)+AKM(I,J,2)*F(I,J,1,NF)
        ELSE
          AP(I,J,1)=AKP(I,J,1)-FLXPK1(I,J)
          CON(I,J,1)=FLXCK1(I,J)
          TEMP=AKM(I,J,2)/AP(I,J,1)
          AP(I,J,2)=AP(I,J,2)-AKP(I,J,1)*TEMP
          CON(I,J,2)=CON(I,J,2)+CON(I,J,1)*TEMP
        ENDIF
        AP(I,J,2)=AP(I,J,2)+AKM(I,J,2)
        AKM(I,J,2)=0.
!ONSIDERA EL PLANO K=N1
        FL=XCVI(I)*F(I,J,N1,3)*RHO(I,J,N1)
        FLM=XCVIP(I-1)*F(I-1,J,N1,3)*RHO(I-1,J,N1)
        FLOW=(FL+FLM)/XCVT
        DIFF=(XCVI(I)*GAM(I,J,N1)+XCVIP(I-1)*GAM(I-1,J,N1))/&
     &       (ZDIF(N1)*XCVT)+SMALL
        CALL DIFLOW
             AKP(I,J,N2)=ACOF+MAX(-FLOW,0.)
             AKM(I,J,N1)=AKP(I,J,N2)+FLOW
             AKP(I,J,N2)=AKP(I,J,N2)*XCVT*YCVR(J)
             AKP(I,J,N1)=0.
        IF(KBCN1(I,J).EQ.1) THEN
          CON(I,J,N2)=CON(I,J,N2)+AKP(I,J,N2)*F(I,J,N1,NF)
        ELSE
          AP(I,J,N1)=AKM(I,J,N1)-FLXPN1(I,J)
          CON(I,J,N1)=FLXCN1(I,J)
          TEMP=AKP(I,J,N2)/AP(I,J,N1)
          AP(I,J,N2)=AP(I,J,N2)-AKM(I,J,N1)*TEMP
          CON(I,J,N2)=CON(I,J,N2)+CON(I,J,N1)*TEMP
        ENDIF
        AP(I,J,N2)=AP(I,J,N2)+AKP(I,J,N2)
        AKP(I,J,N2)=0.
       ENDDO
      ENDDO
!ONSIDERA SUBRELAJACION Y CONSTRUYE AP(I,J,K) Y CON(I,J,K) EN FORMA FINA
      DO K=2,N2
       DO J=2,M2
        DO I=3,L2
         VOL=ZCV(K)*YCVR(J)*XCVS(I)
         ANB=AIP(I,J,K)+AIM(I,J,K)+AJP(I,J,K)+AJM(I,J,K)&
     &      +AKP(I,J,K)+AKM(I,J,K)
         AINR=ANB*RLX
         AP(I,J,K)=AP(I,J,K)+ANB+AINR
         CON(I,J,K)=CON(I,J,K)+AINR*F(I,J,K,NF)
         DU(I,J,K)=VOL/(XDIF(I)*SX(J))
         CON(I,J,K)=CON(I,J,K)+DU(I,J,K)*(P(I-1,J,K)-P(I,J,K))
         DU(I,J,K)=DU(I,J,K)/AP(I,J,K)
        ENDDO
       ENDDO
      ENDDO
!         LLAMA LA RUTINA SOLVE PARA OBTENER LA SOLUCION DE LAS
!                      ECUACIONES DISCRETIZADAS
      CALL SOLVE
   20 CONTINUE
!-----------------------------------------------------------------------
!     COEFICIENTES PARA LA ECUACION DE LA COMPONENTE DE VELOCIDAD "V"
!-----------------------------------------------------------------------
      NF=2
      IF(KSOLVE(NF).EQ.0) GO TO 40
      IST=2
      JST=3
      KST=2
      CALL PHI
      RLX=(1.-RELAX(NF))/RELAX(NF)
!ONSIDERACION DE LOS TERMINOS VOLUMETRICOS
      DO K=2,N2
       DO J=3,M2
        DO I=2,L2
         VOL=ZCV(K)*YCVRS(J)*XCV(I)
         IF(J.NE.M2) THEN
           SXT=SX(J)
         ELSE
           SXT=SX(M1)
         ENDIF
         IF(J.NE.3) THEN
           SXB=SX(J-1)
         ELSE
           SXB=SX(1)
         ENDIF
         APT=(YCVJ(J)*RHO(I,J,K)*0.5*(SXT+SXMN(J))+YCVJP(J-1)*&
     &        RHO(I,J-1,K)*0.5*(SXB+SXMN(J)))/(YCVRS(J)*DT)
         AP(I,J,K)=(APT-AP(I,J,K))*VOL
         CON(I,J,K)=(CON(I,J,K)+APT*FOLD(I,J,K,NF))*VOL
        ENDDO
       ENDDO
      ENDDO

!ALCULO DE LOS COEFICIENTES EN LA DIRECCION X
      LEND=L3
      IF(KCY.NE.0) LEND=L2
      DO K=2,N2
       DO J=3,M2
        DO I=2,LEND
         IFOR=I+1
         IF(I.EQ.L2) IFOR=IST
         FL=YCDJ(J)*F(IFOR,J,K,1)*(FX(IFOR)*RHO(IFOR,J,K)&
     &     +FXM(IFOR)*RHO(I,J,K))
         FLM=YCDJP(J-1)*F(IFOR,J-1,K,1)*(FX(IFOR)*RHO(IFOR,J-1,K)&
     &     +FXM(IFOR)*RHO(I,J-1,K))
         GM=GAM(I,J,K)*GAM(IFOR,J,K)/(XCV(I)*GAM(IFOR,J,K)&
     &     +XCV(IFOR)*GAM(I,J,K)+SMALL)*YCDJ(J)
         GMM=GAM(I,J-1,K)*GAM(IFOR,J-1,K)/(XCV(I)*GAM(IFOR,J-1,K)&
     &     +XCV(IFOR)*GAM(I,J-1,K)+SMALL)*YCDJP(J-1)
         FLOW=ZCV(K)*(FL+FLM)
         DIFF=2.*ZCV(K)*(GM+GMM)/SXMN(J)
         CALL DIFLOW
              AIM(IFOR,J,K)=ACOF+MAX(FLOW,0.)
              AIP(I,J,K)=AIM(IFOR,J,K)-FLOW
        ENDDO
       ENDDO
      ENDDO
      IF(KCY.NE.0) GO TO 50
!ONSIDERA EL PLANO I=1
      DO K=2,N2
       DO J=3,M2
        YCVT=YCDJ(J)+YCDJP(J-1)
        FL=YCDJ(J)*F(2,J,K,1)*RHO(1,J,K)
        FLM=YCDJP(J-1)*F(2,J-1,K,1)*RHO(1,J-1,K)
        FLOW=(FL+FLM)/YCVT
        DIFF=(YCDJ(J)*GAM(1,J,K)+YCDJP(J-1)*GAM(1,J-1,K))/&
     &       (XDIF(2)*YCVT*SXMN(J))+SMALL
        CALL DIFLOW
             AIM(2,J,K)=ACOF+MAX(FLOW,0.)
             AIP(1,J,K)=AIM(2,J,K)-FLOW
             AIM(2,J,K)=AIM(2,J,K)*YCVT*ZCV(K)
             AIM(1,J,K)=0.
        IF(KBCI1(J,K).EQ.1) THEN
          CON(2,J,K)=CON(2,J,K)+AIM(2,J,K)*F(1,J,K,NF)
        ELSE
          AP(1,J,K)=AIP(1,J,K)-FLXPI1(J,K)
          CON(1,J,K)=FLXCI1(J,K)
          TEMP=AIM(2,J,K)/AP(1,J,K)
          AP(2,J,K)=AP(2,J,K)-AIP(1,J,K)*TEMP
          CON(2,J,K)=CON(2,J,K)+CON(1,J,K)*TEMP
        ENDIF
        AP(2,J,K)=AP(2,J,K)+AIM(2,J,K)
        AIM(2,J,K)=0.
!ONSIDERA EL PLANO I=L1
        FL=YCDJ(J)*F(L1,J,K,1)*RHO(L1,J,K)
        FLM=YCDJP(J-1)*F(L1,J-1,K,1)*RHO(L1,J-1,K)
        FLOW=(FL+FLM)/YCVT
        DIFF=(YCDJ(J)*GAM(L1,J,K)+YCDJP(J-1)*GAM(L1,J-1,K))/&
     &       (XDIF(L1)*YCVT*SXMN(J))+SMALL
        CALL DIFLOW
             AIP(L2,J,K)=ACOF+MAX(-FLOW,0.)
             AIM(L1,J,K)=AIP(L2,J,K)+FLOW
             AIP(L2,J,K)=AIP(L2,J,K)*YCVT*ZCV(K)
             AIP(L1,J,K)=0.
        IF(KBCL1(J,K).EQ.1) THEN
          CON(L2,J,K)=CON(L2,J,K)+AIP(L2,J,K)*F(L1,J,K,NF)
        ELSE
          AP(L1,J,K)=AIM(L1,J,K)-FLXPL1(J,K)
          CON(L1,J,K)=FLXCL1(J,K)
          TEMP=AIP(L2,J,K)/AP(L1,J,K)
          AP(L2,J,K)=AP(L2,J,K)-AIM(L1,J,K)*TEMP
          CON(L2,J,K)=CON(L2,J,K)+CON(L1,J,K)*TEMP
        ENDIF
        AP(L2,J,K)=AP(L2,J,K)+AIP(L2,J,K)
        AIP(L2,J,K)=0.
       ENDDO
      ENDDO
   50 CONTINUE
!ALCULO DE LOS COEFICIENTES EN LA DIRECCION Y
      DO K=2,N2
       DO J=3,M3
        DO I=2,L2
         AREA=ZCV(K)*XCV(I)
         FL=F(I,J,K,2)*(FY(J)*RHO(I,J,K)+FYM(J)*RHO(I,J-1,K))*RV(J)
         FLP=F(I,J+1,K,2)*(FY(J+1)*RHO(I,J+1,K)+FYM(J+1)*RHO(I,J,K))*&
     &       RV(J+1)
         FLOW=AREA*(FV(J)*FL+FVP(J)*FLP)
         DIFF=R(J)*AREA*GAM(I,J,K)/YCV(J)+SMALL
         CALL DIFLOW
              AJM(I,J+1,K)=ACOF+MAX(FLOW,0.)
              AJP(I,J,K)=AJM(I,J+1,K)-FLOW
        ENDDO
       ENDDO
      ENDDO
!ONSIDERA EL PLANO J=2 PARA LA VELOCIDAD "V". MALLA DESPLAZADA
      DO K=2,N2
       DO I=2,L2
        AREA=ZCV(K)*XCV(I)
        FLOW=F(I,2,K,2)*RHO(I,1,K)
        DIFF=GAM(I,1,K)/YCV(2)+SMALL
        CALL DIFLOW
             AJM(I,3,K)=ACOF+MAX(FLOW,0.)
             AJP(I,2,K)=AJM(I,3,K)-FLOW
             AJM(I,3,K)=AJM(I,3,K)*R(1)*AREA
             AJM(I,2,K)=0.
        IF(KBCJ1(I,K).EQ.1) THEN
          CON(I,3,K)=CON(I,3,K)+AJM(I,3,K)*F(I,2,K,NF)
        ELSE
          AP(I,2,K)=AJP(I,2,K)-FLXPJ1(I,K)
          CON(I,2,K)=FLXCJ1(I,K)
          TEMP=AJM(I,3,K)/AP(I,2,K)
          AP(I,3,K)=AP(I,3,K)-AJP(I,2,K)*TEMP
          CON(I,3,K)=CON(I,3,K)+CON(I,2,K)*TEMP
        ENDIF
        AP(I,3,K)=AP(I,3,K)+AJM(I,3,K)
        AJM(I,3,K)=0.
!ONSIDERA EL PLANO J=M1
        FLOW=F(I,M1,K,2)*RHO(I,M1,K)
        DIFF=GAM(I,M1,K)/YCV(M2)+SMALL
        CALL DIFLOW
             AJP(I,M2,K)=ACOF+MAX(-FLOW,0.)
             AJM(I,M1,K)=AJP(I,M2,K)+FLOW
             AJP(I,M2,K)=AJP(I,M2,K)*R(M1)*AREA
             AJP(I,M1,K)=0.
        IF(KBCM1(I,K).EQ.1) THEN
          CON(I,M2,K)=CON(I,M2,K)+AJP(I,M2,K)*F(I,M1,K,NF)
        ELSE
          AP(I,M1,K)=AJM(I,M1,K)-FLXPM1(I,K)
          CON(I,M1,K)=FLXCM1(I,K)
          TEMP=AJP(I,M2,K)/AP(I,M1,K)
          AP(I,M2,K)=AP(I,M2,K)-AJM(I,M1,K)*TEMP
          CON(I,M2,K)=CON(I,M2,K)+CON(I,M1,K)*TEMP
        ENDIF
        AP(I,M2,K)=AP(I,M2,K)+AJP(I,M2,K)
        AJP(I,M2,K)=0.
       ENDDO
      ENDDO
!ALCULOS DE LOS COEFICIENTES EN LA DIRECCION Z
      DO K=2,N3
       DO J=3,M2
        DO I=2,L2
         FL=YCVJ(J)*F(I,J,K+1,3)*(FZ(K+1)*RHO(I,J,K+1)&
     &     +FZM(K+1)*RHO(I,J,K))
         FLM=YCVJP(J-1)*F(I,J-1,K+1,3)*(FZ(K+1)*RHO(I,J-1,K+1)&
     &     +FZM(K+1)*RHO(I,J-1,K))
         GM=GAM(I,J,K)*GAM(I,J,K+1)/(ZCV(K)*GAM(I,J,K+1)&
     &     +ZCV(K+1)*GAM(I,J,K)+SMALL)*YCVJ(J)
         GMM=GAM(I,J-1,K)*GAM(I,J-1,K+1)/(ZCV(K)*GAM(I,J-1,K+1)&
     &     +ZCV(K+1)*GAM(I,J-1,K)+SMALL)*YCVJP(J-1)
         FLOW=XCV(I)*(FL+FLM)
         DIFF=2.*XCV(I)*(GM+GMM)
         CALL DIFLOW
              AKM(I,J,K+1)=ACOF+MAX(FLOW,0.)
              AKP(I,J,K)=AKM(I,J,K+1)-FLOW
        ENDDO
       ENDDO
      ENDDO
!ONSIDERA EL PLANO K=1
      DO J=3,M2
       DO I=2,L2
        YCVT=YCVJ(J)+YCVJP(J-1)
        FL=YCVJ(J)*F(I,J,2,3)*RHO(I,J,1)
        FLM=YCVJP(J-1)*F(I,J-1,2,3)*RHO(I,J-1,1)
        FLOW=(FL+FLM)/YCVT
        DIFF=(YCVJ(J)*GAM(I,J,1)+YCVJP(J-1)*GAM(I,J-1,1))/&
     &       (ZDIF(2)*YCVT)+SMALL
        CALL DIFLOW
             AKM(I,J,2)=ACOF+MAX(FLOW,0.)
             AKP(I,J,1)=AKM(I,J,2)-FLOW
             AKM(I,J,2)=AKM(I,J,2)*YCVT*XCV(I)
             AKM(I,J,1)=0.
        IF(KBCK1(I,J).EQ.1) THEN
          CON(I,J,2)=CON(I,J,2)+AKM(I,J,2)*F(I,J,1,NF)
        ELSE
          AP(I,J,1)=AKP(I,J,1)-FLXPK1(I,J)
          CON(I,J,1)=FLXCK1(I,J)
          TEMP=AKM(I,J,2)/AP(I,J,1)
          AP(I,J,2)=AP(I,J,2)-AKP(I,J,1)*TEMP
          CON(I,J,2)=CON(I,J,2)+CON(I,J,1)*TEMP
        ENDIF
        AP(I,J,2)=AP(I,J,2)+AKM(I,J,2)
        AKM(I,J,2)=0.
!ONSIDERA EL PLANO K=N1
        FL=YCVJ(J)*F(I,J,N1,3)*RHO(I,J,N1)
        FLM=YCVJP(J-1)*F(I,J-1,N1,3)*RHO(I,J-1,N1)
        FLOW=(FL+FLM)/YCVT
        DIFF=(YCVJ(J)*GAM(I,J,N1)+YCVJP(J-1)*GAM(I,J-1,N1))/&
     &       (ZDIF(N1)*YCVT)+SMALL
        CALL DIFLOW
             AKP(I,J,N2)=ACOF+MAX(-FLOW,0.)
             AKM(I,J,N1)=AKP(I,J,N2)+FLOW
             AKP(I,J,N2)=AKP(I,J,N2)*YCVT*XCV(I)
             AKP(I,J,N1)=0.
        IF(KBCN1(I,J).EQ.1) THEN
          CON(I,J,N2)=CON(I,J,N2)+AKP(I,J,N2)*F(I,J,N1,NF)
        ELSE
          AP(I,J,N1)=AKM(I,J,N1)-FLXPN1(I,J)
          CON(I,J,N1)=FLXCN1(I,J)
          TEMP=AKP(I,J,N2)/AP(I,J,N1)
          AP(I,J,N2)=AP(I,J,N2)-AKM(I,J,N1)*TEMP
          CON(I,J,N2)=CON(I,J,N2)+CON(I,J,N1)*TEMP
        ENDIF
        AP(I,J,N2)=AP(I,J,N2)+AKP(I,J,N2)
        AKP(I,J,N2)=0.
       ENDDO
      ENDDO
!ONSIDERA SUBRELAJACION Y CONSTRUYE AP(I,J,K) Y CON(I,J,K) EN FORMA FINA
      DO K=2,N2
       DO J=3,M2
        DO I=2,L2
         VOL=ZCV(K)*YCVRS(J)*XCV(I)
         ANB=AIP(I,J,K)+AIM(I,J,K)+AJP(I,J,K)+AJM(I,J,K)&
     &      +AKP(I,J,K)+AKM(I,J,K)
         AINR=ANB*RLX
         AP(I,J,K)=AP(I,J,K)+ANB+AINR
         CON(I,J,K)=CON(I,J,K)+AINR*F(I,J,K,NF)
         DV(I,J,K)=VOL/YDIF(J)
         CON(I,J,K)=CON(I,J,K)+DV(I,J,K)*(P(I,J-1,K)-P(I,J,K))
         DV(I,J,K)=DV(I,J,K)/AP(I,J,K)
        ENDDO
       ENDDO
      ENDDO
!         LLAMA LA RUTINA SOLVE PARA OBTENER LA SOLUCION DE LAS
!                      ECUACIONES DISCRETIZADAS
      CALL SOLVE
   40 CONTINUE
!-----------------------------------------------------------------------
!     COEFICIENTES PARA LA ECUACION DE LA COMPONENTE DE VELOCIDAD "W"
!-----------------------------------------------------------------------
      NF=3
      IF(KSOLVE(NF).EQ.0) GO TO 60
      IST=2
      JST=2
      KST=3
      CALL PHI
      RLX=(1.-RELAX(NF))/RELAX(NF)
!ONSIDERACION DE LOS TERMINOS VOLUMETRICOS
      DO K=3,N2
       DO J=2,M2
        DO I=2,L2
         VOL=ZCVS(K)*YCVR(J)*XCV(I)
         APT=(RHO(I,J,K)*ZCVK(K)+RHO(I,J,K-1)*ZCVKP(K-1))/(ZCVS(K)*DT)
         AP(I,J,K)=(APT-AP(I,J,K))*VOL
         CON(I,J,K)=(CON(I,J,K)+APT*FOLD(I,J,K,NF))*VOL
        ENDDO
       ENDDO
      ENDDO
!ALCULO DE LOS COEFICIENTES EN LA DIRECCION X
      LEND=L3
      IF(KCY.NE.0) LEND=L2
      DO K=3,N2
       DO J=2,M2
        DO I=2,LEND
         IFOR=I+1
         IF(I.EQ.L2) IFOR=IST
         FL=ZCVK(K)*F(IFOR,J,K,1)*(FX(IFOR)*RHO(IFOR,J,K)&
     &     +FXM(IFOR)*RHO(I,J,K))
         FLM=ZCVKP(K-1)*F(IFOR,J,K-1,1)*(FX(IFOR)*RHO(IFOR,J,K-1)&
     &     +FXM(IFOR)*RHO(I,J,K-1))
         GM=GAM(I,J,K)*GAM(IFOR,J,K)/(XCV(I)*GAM(IFOR,J,K)&
     &     +XCV(IFOR)*GAM(I,J,K)+SMALL)*ZCVK(K)
         GMM=GAM(I,J,K-1)*GAM(IFOR,J,K-1)/(XCV(I)*GAM(IFOR,J,K-1)&
     &     +XCV(IFOR)*GAM(I,J,K-1)+SMALL)*ZCVKP(K-1)
         FLOW=YCV(J)*(FL+FLM)
         DIFF=2.*YCV(J)*(GM+GMM)/(SX(J))
         CALL DIFLOW
              AIM(IFOR,J,K)=ACOF+MAX(FLOW,0.)
              AIP(I,J,K)=AIM(IFOR,J,K)-FLOW
        ENDDO
       ENDDO
      ENDDO
      IF(KCY.NE.0) GO TO 70
!ONSIDERA EL PLANO I=1
      DO K=3,N2
       DO J=2,M2
        ZCVT=ZCVK(K)+ZCVKP(K-1)
        FL=ZCVK(K)*F(2,J,K,1)*RHO(1,J,K)
        FLM=ZCVKP(K-1)*F(2,J,K-1,1)*RHO(1,J,K-1)
        FLOW=(FL+FLM)/ZCVT
        DIFF=(ZCVK(K)*GAM(1,J,K)+ZCVKP(K-1)*GAM(1,J,K-1))/&
     &       (XDIF(2)*ZCVT*SX(J)+SMALL)
        CALL DIFLOW
             AIM(2,J,K)=ACOF+MAX(FLOW,0.)
             AIP(1,J,K)=AIM(2,J,K)-FLOW
             AIM(2,J,K)=AIM(2,J,K)*ZCVT*YCV(J)
             AIM(1,J,K)=0.
        IF(KBCI1(J,K).EQ.1) THEN
          CON(2,J,K)=CON(2,J,K)+AIM(2,J,K)*F(1,J,K,NF)
        ELSE
          AP(1,J,K)=AIP(1,J,K)-FLXPI1(J,K)
          CON(1,J,K)=FLXCI1(J,K)
          TEMP=AIM(2,J,K)/AP(1,J,K)
          AP(2,J,K)=AP(2,J,K)-AIP(1,J,K)*TEMP
          CON(2,J,K)=CON(2,J,K)+CON(1,J,K)*TEMP
        ENDIF
        AP(2,J,K)=AP(2,J,K)+AIM(2,J,K)
        AIM(2,J,K)=0.
!ONSIDERA EL PLANO I=L1
        FL=ZCVK(K)*F(L1,J,K,1)*RHO(L1,J,K)
        FLM=ZCVKP(K-1)*F(L1,J,K-1,1)*RHO(L1,J,K-1)
        FLOW=(FL+FLM)/ZCVT
        DIFF=(ZCVK(K)*GAM(L1,J,K)+ZCVKP(K-1)*GAM(L1,J,K-1))/&
     &       (XDIF(L1)*ZCVT*SX(J)+SMALL)
        CALL DIFLOW
             AIP(L2,J,K)=ACOF+MAX(-FLOW,0.)
             AIM(L1,J,K)=AIP(L2,J,K)+FLOW
             AIP(L2,J,K)=AIP(L2,J,K)*ZCVT*YCV(J)
             AIP(L1,J,K)=0.
        IF(KBCL1(J,K).EQ.1) THEN
          CON(L2,J,K)=CON(L2,J,K)+AIP(L2,J,K)*F(L1,J,K,NF)
        ELSE
          AP(L1,J,K)=AIM(L1,J,K)-FLXPL1(J,K)
          CON(L1,J,K)=FLXCL1(J,K)
          TEMP=AIP(L2,J,K)/AP(L1,J,K)
          AP(L2,J,K)=AP(L2,J,K)-AIM(L1,J,K)*TEMP
          CON(L2,J,K)=CON(L2,J,K)+CON(L1,J,K)*TEMP
        ENDIF
        AP(L2,J,K)=AP(L2,J,K)+AIP(L2,J,K)
        AIP(L2,J,K)=0.
       ENDDO
      ENDDO
   70 CONTINUE
!ALCULO DE LOS COEFICIENTES EN LA DIRECCION Y
      DO K=3,N2
       DO J=2,M3
        DO I=2,L2
         AREA=XCV(I)*RV(J+1)
         FL=ZCVK(K)*F(I,J+1,K,2)*(FY(J+1)*RHO(I,J+1,K)&
     &     +FYM(J+1)*RHO(I,J,K))
         FLM=ZCVKP(K-1)*F(I,J+1,K-1,2)*(FY(J+1)*RHO(I,J+1,K-1)&
     &     +FYM(J+1)*RHO(I,J,K-1))
         GM=GAM(I,J,K)*GAM(I,J+1,K)/(YCV(J)*GAM(I,J+1,K)&
     &     +YCV(J+1)*GAM(I,J,K)+SMALL)*ZCVK(K)
         GMM=GAM(I,J,K-1)*GAM(I,J+1,K-1)/(YCV(J)*GAM(I,J+1,K-1)&
     &     +YCV(J+1)*GAM(I,J,K-1)+SMALL)*ZCVKP(K-1)
         FLOW=AREA*(FL+FLM)
         DIFF=2.*AREA*(GM+GMM)
         CALL DIFLOW
              AJM(I,J+1,K)=ACOF+MAX(FLOW,0.)
              AJP(I,J,K)=AJM(I,J+1,K)-FLOW
        ENDDO
       ENDDO
      ENDDO
!ONSIDERA EL PLANO J=1
      DO K=3,N2
       DO I=2,L2
        ZCVT=ZCVK(K)+ZCVKP(K-1)
        FL=ZCVK(K)*F(I,2,K,2)*RHO(I,1,K)
        FLM=ZCVKP(K-1)*F(I,2,K-1,2)*RHO(I,1,K-1)
        FLOW=(FL+FLM)/ZCVT
        DIFF=(ZCVK(K)*GAM(I,1,K)+ZCVKP(K-1)*GAM(I,1,K-1))/&
     &       (YDIF(2)*ZCVT)+SMALL
        CALL DIFLOW
             AJM(I,2,K)=ACOF+MAX(FLOW,0.)
             AJP(I,1,K)=AJM(I,2,K)-FLOW
             AJM(I,2,K)=AJM(I,2,K)*R(1)*ZCVT*XCV(I)
             AJM(I,1,K)=0.
        IF(KBCJ1(I,K).EQ.1) THEN
          CON(I,2,K)=CON(I,2,K)+AJM(I,2,K)*F(I,1,K,NF)
        ELSE
          AP(I,1,K)=AJP(I,1,K)-FLXPJ1(I,K)
          CON(I,1,K)=FLXCJ1(I,K)
          TEMP=AJM(I,2,K)/AP(I,1,K)
          AP(I,2,K)=AP(I,2,K)-AJP(I,1,K)*TEMP
          CON(I,2,K)=CON(I,2,K)+CON(I,1,K)*TEMP
        ENDIF
        AP(I,2,K)=AP(I,2,K)+AJM(I,2,K)
        AJM(I,2,K)=0.
!ONSIDERA EL PLANO J=M1
        FL=ZCVK(K)*F(I,M1,K,2)*RHO(I,M1,K)
        FLM=ZCVKP(K-1)*F(I,M1,K-1,2)*RHO(I,M1,K-1)
        FLOW=(FL+FLM)/ZCVT
        DIFF=(ZCVK(K)*GAM(I,M1,K)+ZCVKP(K-1)*GAM(I,M1,K-1))/&
     &       (YDIF(M1)*ZCVT)+SMALL
        CALL DIFLOW
             AJP(I,M2,K)=ACOF+MAX(-FLOW,0.)
             AJM(I,M1,K)=AJP(I,M2,K)+FLOW
             AJP(I,M2,K)=AJP(I,M2,K)*R(M1)*ZCVT*XCV(I)
             AJP(I,M1,K)=0.
        IF(KBCM1(I,K).EQ.1) THEN
          CON(I,M2,K)=CON(I,M2,K)+AJP(I,M2,K)*F(I,M1,K,NF)
        ELSE
          AP(I,M1,K)=AJM(I,M1,K)-FLXPM1(I,K)
          CON(I,M1,K)=FLXCM1(I,K)
          TEMP=AJP(I,M2,K)/AP(I,M1,K)
          AP(I,M2,K)=AP(I,M2,K)-AJM(I,M1,K)*TEMP
          CON(I,M2,K)=CON(I,M2,K)+CON(I,M1,K)*TEMP
        ENDIF
        AP(I,M2,K)=AP(I,M2,K)+AJP(I,M2,K)
        AJP(I,M2,K)=0.
       ENDDO
      ENDDO
!ALCULO DE LOS COEFICIENTES EN LA DIRECCION Z
      DO K=3,N3
       DO J=2,M2
        DO I=2,L2
         FL=F(I,J,K,3)*(FZ(K)*RHO(I,J,K)+FZM(K)*RHO(I,J,K-1))
         FLP=F(I,J,K+1,3)*(FZ(K+1)*RHO(I,J,K+1)+FZM(K+1)*RHO(I,J,K))
         FLOW=ARZ(I,J)*0.5*(FL+FLP)
         DIFF=ARZ(I,J)*GAM(I,J,K)/ZCV(K)+SMALL
         CALL DIFLOW
              AKM(I,J,K+1)=ACOF+MAX(FLOW,0.)
              AKP(I,J,K)=AKM(I,J,K+1)-FLOW
        ENDDO
       ENDDO
      ENDDO
!ONSIDERA EL PLANO K=2 PARA LA VELOCIDAD "W". MALLA DESPLAZADA.
      DO J=2,M2
       DO I=2,L2
        FLOW=F(I,J,2,3)*RHO(I,J,1)
        DIFF=GAM(I,J,1)/ZCV(2)+SMALL
        CALL DIFLOW
             AKM(I,J,3)=ACOF+MAX(FLOW,0.)
             AKP(I,J,2)=AKM(I,J,3)-FLOW
             AKM(I,J,3)=AKM(I,J,3)*ARZ(I,J)
             AKM(I,J,2)=0.
        IF(KBCK1(I,J).EQ.1) THEN
          CON(I,J,3)=CON(I,J,3)+AKM(I,J,3)*F(I,J,2,NF)
        ELSE
          AP(I,J,2)=AKP(I,J,2)-FLXPK1(I,J)
          CON(I,J,2)=FLXCK1(I,J)
          TEMP=AKM(I,J,3)/AP(I,J,2)
          AP(I,J,3)=AP(I,J,3)-AKP(I,J,2)*TEMP
          CON(I,J,3)=CON(I,J,3)+CON(I,J,2)*TEMP
        ENDIF
        AP(I,J,3)=AP(I,J,3)+AKM(I,J,3)
        AKM(I,J,3)=0.
!ONSIDERA EL PLANO K=N1
        FLOW=F(I,J,N1,3)*RHO(I,J,N1)
        DIFF=GAM(I,J,N1)/ZCV(N2)+SMALL
        CALL DIFLOW
             AKP(I,J,N2)=ACOF+MAX(-FLOW,0.)
             AKM(I,J,N1)=AKP(I,J,N2)+FLOW
      	     AKP(I,J,N2)=AKP(I,J,N2)*ARZ(I,J)
             AKP(I,J,N1)=0.
        IF(KBCN1(I,J).EQ.1) THEN
          CON(I,J,N2)=CON(I,J,N2)+AKP(I,J,N2)*F(I,J,N1,NF)
        ELSE
          AP(I,J,N1)=AKM(I,J,N1)-FLXPN1(I,J)
          CON(I,J,N1)=FLXCN1(I,J)
          TEMP=AKP(I,J,N2)/AP(I,J,N1)
          AP(I,J,N2)=AP(I,J,N2)-AKM(I,J,N1)*TEMP
          CON(I,J,N2)=CON(I,J,N2)+CON(I,J,N1)*TEMP
        ENDIF
        AP(I,J,N2)=AP(I,J,N2)+AKP(I,J,N2)
        AKP(I,J,N2)=0.
       ENDDO
      ENDDO
!ONSIDERA SUBRELAJACION Y CONSTRUYE AP(I,J,K) Y CON(I,J,K) EN FORMA FINA
      DO K=3,N2
       DO J=2,M2
        DO I=2,L2
         VOL=ZCVS(K)*YCVR(J)*XCV(I)
         ANB=AIP(I,J,K)+AIM(I,J,K)+AJP(I,J,K)+AJM(I,J,K)&
     &      +AKP(I,J,K)+AKM(I,J,K)
         AINR=ANB*RLX
         AP(I,J,K)=AP(I,J,K)+ANB+AINR
         CON(I,J,K)=CON(I,J,K)+AINR*F(I,J,K,NF)
         DW(I,J,K)=VOL/ZDIF(K)
         CON(I,J,K)=CON(I,J,K)+DW(I,J,K)*(P(I,J,K-1)-P(I,J,K))
         DW(I,J,K)=DW(I,J,K)/AP(I,J,K)
        ENDDO
       ENDDO
      ENDDO
      CALL SOLVE
!         LLAMA LA RUTINA SOLVE PARA OBTENER LA SOLUCION DE LAS
!                      ECUACIONES DISCRETIZADAS
   60 CONTINUE
      RETURN
      END
!>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
      SUBROUTINE HEART2
!<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
      INCLUDE '3DCOMMON.F90'
!     =================================================================
!ONSTRUCCION DE LAZOS PARA TODAS LAS ECUACIONES EN LOS NODOS PRINCIPALES
      IST=2
      JST=2
      KST=2
      DO N=5,NFMAX
      NF=N
      IF(KSOLVE(NF).EQ.0) GO TO 80
      CALL PHI
!ALCULO DE LOS COEFICIENTES DE LA ECUACION DISCRETIZADA
       BETA=4./3.
       IF(KORD.EQ.1) BETA=1.
       RLX=(1.-RELAX(NF))/RELAX(NF)
!ONSIDERA LOS TERMINOS VOLUMETRICOS
      DO K=2,N2
        DO J=2,M2
          DO I=2,L2
             VOL=ARZ(I,J)*ZCV(K)
             APT=RHO(I,J,K)/DT
             CON(I,J,K)=(CON(I,J,K)+APT*FOLD(I,J,K,NF))*VOL
             AP(I,J,K)=(APT-AP(I,J,K))*VOL
          ENDDO
        ENDDO
      ENDDO
!OEFICIENTES DE LA DIFUSION EN LA DIRECCION X
      LEND=L3
      IF(KCY.NE.0) LEND=L2
      DO K=2,N2
        DO J=2,M2
          DO I=2,LEND
             IFOR=I+1
             IF(I.EQ.L2) IFOR=2
             FLOW=ARX(J,K)*F(IFOR,J,K,1)*(FX(IFOR)*RHO(IFOR,J,K)+&
     &            FXM(IFOR)*RHO(I,J,K))
             DIFF=ARX(J,K)*2.*GAM(I,J,K)*GAM(IFOR,J,K)/((XCV(I)*&
     &            GAM(IFOR,J,K)+XCV(IFOR)*GAM(I,J,K)+SMALL)*SX(J))
             CALL DIFLOW
                  AIM(IFOR,J,K)=ACOF+MAX(0.,FLOW)
                  AIP(I,J,K)=AIM(IFOR,J,K)-FLOW
          ENDDO
        ENDDO
      ENDDO
      IF(KCY.NE.0) GO TO 90
      DO K=2,N2
        DO J=2,M2
!     CONSIDERA EL PLANO I=1
           FLOW=F(2,J,K,1)*RHO(1,J,K)
           DIFF=GAM(1,J,K)/(XDIF(2)*SX(J))
           CALL DIFLOW
                AIM(2,J,K)=BETA*ACOF+MAX(0.,FLOW)
                AIP(1,J,K)=AIM(2,J,K)-FLOW
                AIM(2,J,K)=AIM(2,J,K)*ARX(J,K)
                AIM(1,J,K)=(BETA-1.)*((AIP(2,J,K)/&
     &                     ARX(J,K))+(FLOW/ARX(J,K)))
                AIP(2,J,K)=AIP(2,J,K)+AIM(1,J,K)*ARX(J,K)
           IF(KBCI1(J,K).EQ.1) THEN
             CON(2,J,K)=CON(2,J,K)+AIM(2,J,K)*F(1,J,K,NF)
           ELSE
             AP(1,J,K)=AIP(1,J,K)-FLXPI1(J,K)
             CON(1,J,K)=FLXCI1(J,K)
             TEMP=AIM(2,J,K)/AP(1,J,K)
             AP(2,J,K)=AP(2,J,K)-AIP(1,J,K)*TEMP
             AIP(2,J,K)=AIP(2,J,K)-AIM(1,J,K)*TEMP
             CON(2,J,K)=CON(2,J,K)+CON(1,J,K)*TEMP
           ENDIF
             AP(2,J,K)=AP(2,J,K)+AIM(2,J,K)
             AIM(2,J,K)=0.
!     CONSIDERA EL PLANO I=L1
           FLOW=F(L1,J,K,1)*RHO(L1,J,K)
           DIFF=GAM(L1,J,K)/(XDIF(L1)*SX(J))+SMALL
           CALL DIFLOW
                AIP(L2,J,K)=BETA*ACOF+MAX(0.,-FLOW)
                AIM(L1,J,K)=AIP(L2,J,K)+FLOW
                AIP(L2,J,K)=AIP(L2,J,K)*ARX(J,K)
                AIP(L1,J,K)=(BETA-1.)*((AIM(L2,J,K)/&
     &                      ARX(J,K))-(FLOW/ARX(J,K)))
                AIM(L2,J,K)=AIM(L2,J,K)+AIP(L1,J,K)*ARX(J,K)
           IF(KBCL1(J,K).EQ.1) THEN
             CON(L2,J,K)=CON(L2,J,K)+AIP(L2,J,K)*F(L1,J,K,NF)
           ELSE
             AP(L1,J,K)=AIM(L1,J,K)-FLXPL1(J,K)
             CON(L1,J,K)=FLXCL1(J,K)
             TEMP=AIP(L2,J,K)/AP(L1,J,K)
             AP(L2,J,K)=AP(L2,J,K)-AIM(L1,J,K)*TEMP
             AIM(L2,J,K)=AIM(L2,J,K)-AIP(L1,J,K)*TEMP
             CON(L2,J,K)=CON(L2,J,K)+CON(L1,J,K)*TEMP
           ENDIF
             AP(L2,J,K)=AP(L2,J,K)+AIP(L2,J,K)
             AIP(L2,J,K)=0.
        ENDDO
      ENDDO
   90 CONTINUE
!     COEFICIENTES DE LA DIFUSION EN LA DIRECCION Y
      DO K=2,N2
        DO J=2,M3
          DO I=2,L2
             AREA=RV(J+1)*XCV(I)*ZCV(K)
             FLOW=AREA*F(I,J+1,K,2)*(FY(J+1)*RHO(I,J+1,K)+&
     &            FYM(J+1)*RHO(I,J,K))
             DIFF=AREA*2.*GAM(I,J,K)*GAM(I,J+1,K)/(YCV(J)*&
     &            GAM(I,J+1,K)+YCV(J+1)*GAM(I,J,K)+SMALL)
             CALL DIFLOW
                  AJM(I,J+1,K)=ACOF+MAX(0.,FLOW)
                  AJP(I,J,K)=AJM(I,J+1,K)-FLOW
          ENDDO
        ENDDO
      ENDDO
      DO K=2,N2
        DO I=2,L2
!     CONSIDERA EL PLANO J=1
           FLOW=F(I,2,K,2)*RHO(I,1,K)
           AREA=RV(2)*XCV(I)*ZCV(K)
           DIFF=GAM(I,1,K)/(YDIF(2))+SMALL
           CALL DIFLOW
                AJM(I,2,K)=BETA*ACOF+MAX(0.,FLOW)
                AJP(I,1,K)=AJM(I,2,K)-FLOW
                AJM(I,2,K)=AJM(I,2,K)*AREA
                AJM(I,1,K)=(BETA-1.)*((AJP(I,2,K)/(RV(3)*XCV(I)*ZCV(K)))&
     &                     +FLOW/(RV(3)*XCV(I)*ZCV(K))+SMALL)
                AJP(I,2,K)=AJP(I,2,K)+AJM(I,1,K)*AREA
           IF(KBCJ1(I,K).EQ.1) THEN
             CON(I,2,K)=CON(I,2,K)+AJM(I,2,K)*F(I,1,K,NF)
           ELSE
             AP(I,1,K)=AJP(I,1,K)-FLXPJ1(I,K)
             CON(I,1,K)=FLXCJ1(I,K)
             TEMP=AJM(I,2,K)/AP(I,1,K)
             AP(I,2,K)=AP(I,2,K)-AJP(I,1,K)*TEMP
             AJP(I,2,K)=AJP(I,2,K)-AJM(I,1,K)*TEMP
             CON(I,2,K)=CON(I,2,K)+CON(I,1,K)*TEMP
           ENDIF
             AP(I,2,K)=AP(I,2,K)+AJM(I,2,K)
             AJM(I,2,K)=0.
!     CONSIDERA EL PLANO J=M1
           FLOW=F(I,M1,K,2)*RHO(I,M1,K)
           AREA=RV(M1)*XCV(I)*ZCV(K)
           DIFF=GAM(I,M1,K)/(YDIF(M1))+SMALL
           CALL DIFLOW
                AJP(I,M2,K)=BETA*ACOF+MAX(0.,-FLOW)
                AJM(I,M1,K)=AJP(I,M2,K)+FLOW
                AJP(I,M2,K)=AJP(I,M2,K)*AREA
                AJP(I,M1,K)=(BETA-1.)*((AJM(I,M2,K)/(RV(M2)*XCV(I)*&
     &                      ZCV(K)))-FLOW/(RV(M2)*XCV(I)*ZCV(K))+SMALL)
                AJM(I,M2,K)=AJM(I,M2,K)+AJP(I,M1,K)*AREA
           IF(KBCM1(I,K).EQ.1) THEN
             CON(I,M2,K)=CON(I,M2,K)+AJP(I,M2,K)*F(I,M1,K,NF)
           ELSE
             AP(I,M1,K)=AJM(I,M1,K)-FLXPM1(I,K)
             CON(I,M1,K)=FLXCM1(I,K)
             TEMP=AJP(I,M2,K)/AP(I,M1,K)
             AP(I,M2,K)=AP(I,M2,K)-AJM(I,M1,K)*TEMP
             AJM(I,M2,K)=AJM(I,M2,K)-AJP(I,M1,K)*TEMP
             CON(I,M2,K)=CON(I,M2,K)+CON(I,M1,K)*TEMP
           ENDIF
             AP(I,M2,K)=AP(I,M2,K)+AJP(I,M2,K)
             AJP(I,M2,K)=0.
        ENDDO
      ENDDO
!OEFICIENTES DE LA DIFUSION EN LA DIRECCION Z
      DO J=2,M2
        DO I=2,L2
          DO K=2,N3
             FLOW=ARZ(I,J)*F(I,J,K+1,3)*(FZ(K+1)*RHO(I,J,K+1)+&
     &            FZM(K+1)*RHO(I,J,K))
             DIFF=ARZ(I,J)*2.*GAM(I,J,K)*GAM(I,J,K+1)/(ZCV(K)*&
     &            GAM(I,J,K+1)+ZCV(K+1)*GAM(I,J,K)+SMALL)
             CALL DIFLOW
                  AKM(I,J,K+1)=ACOF+MAX(0.,FLOW)
                  AKP(I,J,K)=AKM(I,J,K+1)-FLOW
          ENDDO
        ENDDO
      ENDDO
      DO J=2,M2
        DO I=2,L2
!     CONSIDERA EL PLANO K=1
           FLOW=F(I,J,2,3)*RHO(I,J,1)
           DIFF=GAM(I,J,1)/(ZDIF(2))+SMALL
           CALL DIFLOW
                AKM(I,J,2)=BETA*ACOF+MAX(0.,FLOW)
                AKP(I,J,1)=AKM(I,J,2)-FLOW
                AKM(I,J,2)=AKM(I,J,2)*ARZ(I,J)
                AKM(I,J,1)=(BETA-1.)*((AKP(I,J,2)/ARZ(I,J))+&
     &                     (FLOW/ARZ(I,J)))
                AKP(I,J,2)=AKP(I,J,2)+AKM(I,J,1)*ARZ(I,J)
           IF(KBCK1(I,J).EQ.1) THEN
             CON(I,J,2)=CON(I,J,2)+AKM(I,J,2)*F(I,J,1,NF)
           ELSE
             AP(I,J,1)=AKP(I,J,1)-FLXPK1(I,J)
             CON(I,J,1)=FLXCK1(I,J)
             TEMP=AKM(I,J,2)/AP(I,J,1)
             AP(I,J,2)=AP(I,J,2)-AKP(I,J,1)*TEMP
             AKP(I,J,2)=AKP(I,J,2)-AKM(I,J,1)*TEMP
             CON(I,J,2)=CON(I,J,2)+CON(I,J,1)*TEMP
           ENDIF
             AP(I,J,2)=AP(I,J,2)+AKM(I,J,2)
             AKM(I,J,2)=0.
!     CONSIDERA EL PLANO K=N1
           FLOW=F(I,J,N1,3)*RHO(I,J,N1)
           DIFF=GAM(I,J,N1)/(ZDIF(N1))+SMALL
           CALL DIFLOW
                AKP(I,J,N2)=BETA*ACOF+MAX(0.,-FLOW)
                AKM(I,J,N1)=AKP(I,J,N2)+FLOW
                AKP(I,J,N2)=AKP(I,J,N2)*ARZ(I,J)
                AKP(I,J,N1)=(BETA-1.)*((AKM(I,J,N2)/ARZ(I,J))&
     &                      -(FLOW/ARZ(I,J)))
                AKM(I,J,N2)=AKM(I,J,N2)+AKP(I,J,N1)*ARZ(I,J)
           IF(KBCN1(I,J).EQ.1) THEN
             CON(I,J,N2)=CON(I,J,N2)+AKP(I,J,N2)*F(I,J,N1,NF)
           ELSE
             AP(I,J,N1)=AKM(I,J,N1)-FLXPN1(I,J)
             CON(I,J,N1)=FLXCN1(I,J)
             TEMP=AKP(I,J,N2)/AP(I,J,N1)
             AP(I,J,N2)=AP(I,J,N2)-AKM(I,J,N1)*TEMP
             AKM(I,J,N2)=AKM(I,J,N2)-AKP(I,J,N1)*TEMP
             CON(I,J,N2)=CON(I,J,N2)+CON(I,J,N1)*TEMP
           ENDIF
             AP(I,J,N2)=AP(I,J,N2)+AKP(I,J,N2)
             AKP(I,J,N2)=0.
        ENDDO
      ENDDO
!ONSTRUYE AP(I,J,K) Y CON(I,J,K) EN FORMA FINAL.INTRODUCE SUBRRELAJACION
      DO K=2,N2
        DO J=2,M2
          DO I=2,L2
             ANB=AIP(I,J,K)+AIM(I,J,K)+AJP(I,J,K)+AJM(I,J,K)+&
     &           AKP(I,J,K)+AKM(I,J,K)
             AINR=ANB*RLX
             AP(I,J,K)=AP(I,J,K)+ANB+AINR
             CON(I,J,K)=CON(I,J,K)+AINR*F(I,J,K,NF)
          ENDDO
        ENDDO
      ENDDO
!         LLAMA LA RUTINA SOLVE PARA OBTENER LA SOLUCION DE LAS
!                      ECUACIONES DISCRETIZADAS
      CALL SOLVE
   80 ENDDO
      RETURN
      END
!CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
        SUBROUTINE SOLVE
!***********************************************************************
      INCLUDE '3DCOMMON.F90'
      DIMENSION RT(8)
!***********************************************************************
      BIG1=1.E+10
      SMALL1=1.0E-5
      KSTF=KST-1
      JSTF=JST-1
      ISTF=IST-1
      LL2=2*L2
      LL=LL2-IST
      MM2=2*M2
      MM=MM2-JST
      NN2=2*N2
      NN=NN2-KST
      N=NF
      NTM=NTIMES(N)
      DO 999 NT=1,NTM
      NTT=NT
      ICON=1
      DO 35 K=KST,N2
      DO 35 J=JST,M2
      DO 35 I=IST,L2
      IF(AP(I,J,K).LT.BIG1) THEN
      IFOR=I+1
      IBAC=I-1
      IF(KCY.NE.0.AND.I.EQ.2) IBAC=L2
      IF(KCY.NE.0.AND.I.EQ.L2) IFOR=2

!RITERIO DE CONVERGENCIA PARA LA RUTINA DE SOLUCION
      RT(1)=AIP(I,J,K)*F(IFOR,J,K,N)
      RT(2)=AIM(I,J,K)*F(IBAC,J,K,N)
      RT(3)=AJP(I,J,K)*F(I,J+1,K,N)
      RT(4)=AJM(I,J,K)*F(I,J-1,K,N)
      RT(5)=AKP(I,J,K)*F(I,J,K+1,N)
      RT(6)=AKM(I,J,K)*F(I,J,K-1,N)
      RT(7)=-AP(I,J,K)*F(I,J,K,N)
      RT(8)=CON(I,J,K)
      RES=0.
      TERM=1.0E-8
      DO 30 IRT=1,8
      RES=RES+RT(IRT)
   30 TERM=MAX(TERM,ABS(RT(IRT)))
      IF(ABS(RES/TERM).GT.CRIT(N))ICON=0
      ENDIF
   35 CONTINUE
      IF(NTT.NE.1.AND.ICON.EQ.1) GO TO 990
      IF(KBLOC(NF).EQ.0) GO TO 80

!  EFECTUA LA CORRECCION DE BLOQUE EN LA DIRECCION I
!-----------------------------------------------------------------------
      IF(KCY.NE.0) THEN
      DO 200 I=IST,L2
      IFOR=I+1
      IBAC=I-1
      IF(I.EQ.2) IBAC=L2
      IF(I.EQ.L2) IFOR=2
      BL=SMALL
      BLP=0.
      BLM=0.
      BLC=0.
      DO 210 K=KST,N2
      DO 210 J=JST,M2
      IF(AP(I,J,K).LT.BIG1) THEN
      BL=BL+AP(I,J,K)
      IF(AP(I,J+1,K).LT.BIG1) BL=BL-AJP(I,J,K)
      IF(AP(I,J-1,K).LT.BIG1) BL=BL-AJM(I,J,K)
      IF(AP(I,J,K+1).LT.BIG1) BL=BL-AKP(I,J,K)
      IF(AP(I,J,K-1).LT.BIG1) BL=BL-AKM(I,J,K)
      IF(AP(IFOR,J,K).LT.BIG1) BLP=BLP+AIP(I,J,K)
      IF(AP(IBAC,J,K).LT.BIG1) BLM=BLM+AIM(I,J,K)
      BLC=BLC+CON(I,J,K)+AIP(I,J,K)*F(IFOR,J,K,N)&
     &                  +AIM(I,J,K)*F(IBAC,J,K,N)&
     &                  +AJP(I,J,K)*F(I,J+1,K,N)+AJM(I,J,K)*F(I,J-1,K,N)&
     &                  +AKP(I,J,K)*F(I,J,K+1,N)+AKM(I,J,K)*F(I,J,K-1,N)&
     &                  -AP(I,J,K)*F(I,J,K,N)
      ENDIF
  210 CONTINUE
      IF(I.EQ.L2) THEN
      PX(IST)=BL
      QX(IST)=BLP
      RX(IST)=BLC
      CN1=BLM
      ENDIF
      IF(I.EQ.IST) THEN
      EX(IST)=BLP/BL
      HX(IST)=BLM/BL
      GX(IST)=BLC/BL
      ENDIF
      IF(I.GT.IST.AND.I.LT.L2) THEN
      DENOM=BL-BLM*EX(IBAC)
      IF(ABS(DENOM/BL).LT.SMALL1) DENOM=BIG
      EX(I)=BLP/DENOM
      HX(I)=BLM*HX(IBAC)/DENOM
      GX(I)=(BLC+BLM*GX(IBAC))/DENOM
      ENDIF
  200 CONTINUE
      DO 220 I=IST+1,L3
      PX(I)=PX(I-1)-QX(I-1)*HX(I-1)
      QX(I)=QX(I-1)*EX(I-1)
  220 RX(I)=RX(I-1)-QX(I-1)*GX(I-1)
      BLN1=((QX(L3)+CN1)*GX(L3)+RX(L3))/&
     &	   (PX(L3)-(QX(L3)+CN1)*(EX(L3)+HX(L3))+SMALL)
      DO 230 I=L2,IST,-1
      IF(I.EQ.L2) THEN
      BL=BLN1
      ELSE
      BL=EX(I)*BL+HX(I)*BLN1+GX(I)
      ENDIF
      DO 230 K=KST,N2
      DO 230 J=JST,M2
      IF(AP(I,J,K).LT.BIG1) F(I,J,K,N)=F(I,J,K,N)+BL
  230 CONTINUE
      ELSE
      PTX(ISTF)=0.
      QTX(ISTF)=0.
      DO 10 I=IST,L2
      BL=SMALL
      BLP=0.
      BLM=0.
      BLC=0.
      DO 20 K=KST,N2
      DO 20 J=JST,M2
      IF(AP(I,J,K).LT.BIG1) THEN
      BL=BL+AP(I,J,K)
      IF(AP(I,J+1,K).LT.BIG1) BL=BL-AJP(I,J,K)
      IF(AP(I,J-1,K).LT.BIG1) BL=BL-AJM(I,J,K)
      IF(AP(I,J,K+1).LT.BIG1) BL=BL-AKP(I,J,K)
      IF(AP(I,J,K-1).LT.BIG1) BL=BL-AKM(I,J,K)
      IF(AP(I+1,J,K).LT.BIG1) BLP=BLP+AIP(I,J,K)
      IF(AP(I-1,J,K).LT.BIG1) BLM=BLM+AIM(I,J,K)
      BLC=BLC+CON(I,J,K)+AIP(I,J,K)*F(I+1,J,K,N)+AIM(I,J,K)*F(I-1,J,K,N)&
     &                  +AJP(I,J,K)*F(I,J+1,K,N)+AJM(I,J,K)*F(I,J-1,K,N)&
     &                  +AKP(I,J,K)*F(I,J,K+1,N)+AKM(I,J,K)*F(I,J,K-1,N)&
     &                  -AP(I,J,K)*F(I,J,K,N)
      ENDIF
   20 CONTINUE
      DENOM=BL-PTX(I-1)*BLM
      IF(ABS(DENOM/BL).LT.SMALL1) DENOM=BIG
      PTX(I)=BLP/DENOM
      QTX(I)=(BLC+BLM*QTX(I-1))/DENOM
   10 CONTINUE
      BL=0.
      DO 40 I=L2,IST,-1
      BL=BL*PTX(I)+QTX(I)
      DO 40 K=KST,N2
      DO 40 J=JST,M2
      IF(AP(I,J,K).LT.BIG1) F(I,J,K,N)=F(I,J,K,N)+BL
   40 CONTINUE
      ENDIF
!  EFECTUA LA CORRECCION DE BLOQUE EN LA DIRECCION J
!-----------------------------------------------------------------------
      PTY(JSTF)=0.
      QTY(JSTF)=0.
      DO 50 J=JST,M2
      BL=SMALL
      BLP=0.
      BLM=0.
      BLC=0.
      DO 60 K=KST,N2
      DO 60 I=IST,L2
      IF(AP(I,J,K).LT.BIG1) THEN
      IFOR=I+1
      IBAC=I-1
      IF(KCY.NE.0.AND.I.EQ.2) IBAC=L2
      IF(KCY.NE.0.AND.I.EQ.L2) IFOR=2
      BL=BL+AP(I,J,K)
      IF(AP(IFOR,J,K).LT.BIG1) BL=BL-AIP(I,J,K)
      IF(AP(IBAC,J,K).LT.BIG1) BL=BL-AIM(I,J,K)
      IF(AP(I,J,K+1).LT.BIG1) BL=BL-AKP(I,J,K)
      IF(AP(I,J,K-1).LT.BIG1) BL=BL-AKM(I,J,K)
      IF(AP(I,J+1,K).LT.BIG1) BLP=BLP+AJP(I,J,K)
      IF(AP(I,J-1,K).LT.BIG1) BLM=BLM+AJM(I,J,K)
      BLC=BLC+CON(I,J,K)+AIP(I,J,K)*F(IFOR,J,K,N)&
     &                  +AIM(I,J,K)*F(IBAC,J,K,N)&
     &                  +AJP(I,J,K)*F(I,J+1,K,N)+AJM(I,J,K)*F(I,J-1,K,N)&
     &                  +AKP(I,J,K)*F(I,J,K+1,N)+AKM(I,J,K)*F(I,J,K-1,N)&
     &                  -AP(I,J,K)*F(I,J,K,N)
      ENDIF
   60 CONTINUE
      DENOM=BL-PTY(J-1)*BLM
      IF(ABS(DENOM/BL).LT.SMALL1) DENOM=BIG
      PTY(J)=BLP/DENOM
      QTY(J)=(BLC+BLM*QTY(J-1))/(DENOM+SMALL)
   50 CONTINUE
      BL=0.
      DO 70 J=M2,JST,-1
      BL=BL*PTY(J)+QTY(J)
      DO 70 K=KST,N2
      DO 70 I=IST,L2
      IF(AP(I,J,K).LT.BIG1) F(I,J,K,N)=F(I,J,K,N)+BL
   70 CONTINUE

!  EFECTUA LA CORRECCION DE BLOQUE EN LA DIRECCION K
!-----------------------------------------------------------------------
      PTZ(KSTF)=0.
      QTZ(KSTF)=0.
      DO 55 K=KST,N2
      BL=SMALL
      BLP=0.
      BLM=0.
      BLC=0.
      DO 65 J=JST,M2
      DO 65 I=IST,L2
      IF(AP(I,J,K).LT.BIG1) THEN
      IFOR=I+1
      IBAC=I-1
      IF(KCY.NE.0.AND.I.EQ.2) IBAC=L2
      IF(KCY.NE.0.AND.I.EQ.L2) IFOR=2
      BL=BL+AP(I,J,K)
      IF(AP(IFOR,J,K).LT.BIG1) BL=BL-AIP(I,J,K)
      IF(AP(IBAC,J,K).LT.BIG1) BL=BL-AIM(I,J,K)
      IF(AP(I,J+1,K).LT.BIG1) BL=BL-AJP(I,J,K)
      IF(AP(I,J-1,K).LT.BIG1) BL=BL-AJM(I,J,K)
      IF(AP(I,J,K+1).LT.BIG1) BLP=BLP+AKP(I,J,K)
      IF(AP(I,J,K-1).LT.BIG1) BLM=BLM+AKM(I,J,K)
      BLC=BLC+CON(I,J,K)+AIP(I,J,K)*F(IFOR,J,K,N)&
     &                  +AIM(I,J,K)*F(IBAC,J,K,N)&
     &                  +AJP(I,J,K)*F(I,J+1,K,N)+AJM(I,J,K)*F(I,J-1,K,N)&
     &                  +AKP(I,J,K)*F(I,J,K+1,N)+AKM(I,J,K)*F(I,J,K-1,N)&
     &                  -AP(I,J,K)*F(I,J,K,N)
      ENDIF
   65 CONTINUE
      DENOM=BL-PTZ(K-1)*BLM
      IF(ABS(DENOM/BL).LT.SMALL1) DENOM=BIG
      PTZ(K)=BLP/DENOM
      QTZ(K)=(BLC+BLM*QTZ(K-1))/DENOM
   55 CONTINUE
      BL=0.
      DO 75 K=N2,KST,-1
      BL=BL*PTZ(K)+QTZ(K)
      DO 75 J=JST,M2
      DO 75 I=IST,L2
      IF(AP(I,J,K).LT.BIG1) F(I,J,K,N)=F(I,J,K,N)+BL
   75 CONTINUE
   80 CONTINUE

!  EJECUTA EL TDMA EN LA DIRECCION I
!-----------------------------------------------------------------------
      DO 90 KK=KST,NN
      K=MIN(KK,NN2-KK)
      DO 90 JJ=JST,MM
      J=MIN(JJ,MM2-JJ)
      IF(KCY.NE.0) THEN
      DENOM=AP(IST,J,K)+SMALL
      EX(IST)=AIP(IST,J,K)/DENOM
      HX(IST)=AIM(IST,J,K)/DENOM
      GX(IST)=(CON(IST,J,K)+AJP(IST,J,K)*F(IST,J+1,K,N)&
     &                     +AJM(IST,J,K)*F(IST,J-1,K,N)&
     &                     +AKP(IST,J,K)*F(IST,J,K+1,N)&
     &                     +AKM(IST,J,K)*F(IST,J,K-1,N))/DENOM
      PX(IST)=AP(L2,J,K)
      QX(IST)=AIP(L2,J,K)
      RX(IST)=CON(L2,J,K)+AJP(L2,J,K)*F(L2,J+1,K,N)&
     &                   +AJM(L2,J,K)*F(L2,J-1,K,N)&
     &                   +AKP(L2,J,K)*F(L2,J,K+1,N)&
     &                   +AKM(L2,J,K)*F(L2,J,K-1,N)
      DO 105 I=IST+1 ,L3
      DENOM=AP(I,J,K)-AIM(I,J,K)*EX(I-1)
      EX(I)=AIP(I,J,K)/DENOM
      HX(I)=AIM(I,J,K)*HX(I-1)/DENOM
      TEMP=CON(I,J,K)+AJP(I,J,K)*F(I,J+1,K,N)+AJM(I,J,K)*F(I,J-1,K,N)&
     &               +AKP(I,J,K)*F(I,J,K+1,N)+AKM(I,J,K)*F(I,J,K-1,N)
      GX(I)=(TEMP+AIM(I,J,K)*GX(I-1))/DENOM
      PX(I)=PX(I-1)-QX(I-1)*HX(I-1)
      QX(I)=QX(I-1)*EX(I-1)
      RX(I)=RX(I-1)+QX(I-1)*GX(I-1)
  105 CONTINUE
      F(L2,J,K,N)=((QX(L3)+AIM(L2,J,K))*GX(L3)+RX(L3))/&
     &            (PX(L3)-(QX(L3)+AIM(L2,J,K))*(EX(L3)+HX(L3))+SMALL)
      DO 115 I=L3,IST,-1
  115 F(I,J,K,N)=EX(I)*F(I+1,J,K,N)+HX(I)*F(L2,J,K,N)+GX(I)
      ELSE
      PTX(ISTF)=0.
      QTX(ISTF)=0.
      DO 100 I=IST,L2
      DENOM=AP(I,J,K)-PTX(I-1)*AIM(I,J,K)
      PTX(I)=AIP(I,J,K)/(DENOM+SMALL)
      TEMP=CON(I,J,K)+AJP(I,J,K)*F(I,J+1,K,N)+AJM(I,J,K)*F(I,J-1,K,N)&
     &               +AKP(I,J,K)*F(I,J,K+1,N)+AKM(I,J,K)*F(I,J,K-1,N)
      QTX(I)=(TEMP+AIM(I,J,K)*QTX(I-1))/(DENOM+SMALL)
  100 CONTINUE
      DO 110 I=L2,IST,-1
  110 F(I,J,K,N)=F(I+1,J,K,N)*PTX(I)+QTX(I)
      ENDIF
   90 CONTINUE

!  EJECUTA EL TDMA EN LA DIRECCION J
!-----------------------------------------------------------------------
      DO 120 II=IST,LL
      I=MIN(II,LL2-II)
      IFOR=I+1
      IBAC=I-1
      IF(KCY.NE.0.AND.I.EQ.2) IBAC=L2
      IF(KCY.NE.0.AND.I.EQ.L2) IFOR=2
      DO 120 KK=KST,NN
      K=MIN(KK,NN2-KK)
      PTY(JSTF)=0.
      QTY(JSTF)=0.
      DO 130 J=JST,M2
      DENOM=AP(I,J,K)-PTY(J-1)*AJM(I,J,K)
      PTY(J)=AJP(I,J,K)/(DENOM+small)
      TEMP=CON(I,J,K)+AIP(I,J,K)*F(IFOR,J,K,N)&
     &               +AIM(I,J,K)*F(IBAC,J,K,N)&
     &               +AKP(I,J,K)*F(I,J,K+1,N)+AKM(I,J,K)*F(I,J,K-1,N)
      QTY(J)=(TEMP+AJM(I,J,K)*QTY(J-1))/(DENOM+SMALL)
  130 CONTINUE
      DO 140 J=M2,JST,-1
  140 F(I,J,K,N)=F(I,J+1,K,N)*PTY(J)+QTY(J)
  120 CONTINUE

!  EJECUTA EL TDMA EN LA DIRECCION K
!-----------------------------------------------------------------------
      DO 125 JJ=JST,MM
      J=MIN(JJ,MM2-JJ)
      DO 125 II=IST,LL
      I=MIN(II,LL2-II)
      IFOR=I+1
      IBAC=I-1
      IF(KCY.NE.0.AND.I.EQ.2) IBAC=L2
      IF(KCY.NE.0.AND.I.EQ.L2) IFOR=2
      PTZ(KSTF)=0.
      QTZ(KSTF)=0.
      DO 135 K=KST,N2
      DENOM=AP(I,J,K)-PTZ(K-1)*AKM(I,J,K)
      PTZ(K)=AKP(I,J,K)/(DENOM+small)
      TEMP=CON(I,J,K)+AIP(I,J,K)*F(IFOR,J,K,N)&
     &               +AIM(I,J,K)*F(IBAC,J,K,N)&
     &               +AJP(I,J,K)*F(I,J+1,K,N)+AJM(I,J,K)*F(I,J-1,K,N)
      QTZ(K)=(TEMP+AKM(I,J,K)*QTZ(K-1))/(DENOM+SMALL)
  135 CONTINUE
      DO 145 K=N2,KST,-1
  145 F(I,J,K,N)=F(I,J,K+1,N)*PTZ(K)+QTZ(K)
  125 CONTINUE
!-----------------------------------------------------------------------
  999 CONTINUE
      NTC(N)=NTT
      GO TO 991
  990 NTC(N)=NTT-1
  991 CONTINUE

!ALCULA LOS VALORES Y FLUJOS DESCONOCIDOS EN LOS BORDES
!-----------------------------------------------------------------------
      DO 165 I=IST,L2
      DO 165 J=JST,M2
      TEMP=AKM(I,J,KSTF)*(F(I,J,KST+1,N)-F(I,J,KST,N))
      IF(KBCK1(I,J).EQ.2)&
     & F(I,J,KSTF,N)=(AKP(I,J,KSTF)*F(I,J,KST,N)-TEMP+CON(I,J,KSTF))&
     & /(AP(I,J,KSTF)+SMALL)
      FLUXK1(I,J,N)=AKP(I,J,KSTF)*(F(I,J,KSTF,N)-F(I,J,KST,N))+TEMP
      TEMP=AKP(I,J,N1)*(F(I,J,N3,N)-F(I,J,N2,N))
      IF(KBCN1(I,J).EQ.2)&
     & F(I,J,N1,N)=(AKM(I,J,N1)*F(I,J,N2,N)-TEMP+CON(I,J,N1))&
     &/(AP(I,J,N1)+SMALL)
  165 FLUXN1(I,J,N)=AKM(I,J,N1)*(F(I,J,N1,N)-F(I,J,N2,N))+TEMP
      DO 160 I=IST,L2
      DO 160 K=KST,N2
      TEMP=AJM(I,JSTF,K)*(F(I,JST+1,K,N)-F(I,JST,K,N))
      IF(KBCJ1(I,K).EQ.2)&
     & F(I,JSTF,K,N)=(AJP(I,JSTF,K)*F(I,JST,K,N)-TEMP+CON(I,JSTF,K))&
     & /(AP(I,JSTF,K)+small)
      FLUXJ1(I,K,N)=AJP(I,JSTF,K)*(F(I,JSTF,K,N)-F(I,JST,K,N))+TEMP
      TEMP=AJP(I,M1,K)*(F(I,M3,K,N)-F(I,M2,K,N))
      IF(KBCM1(I,K).EQ.2)&
     & F(I,M1,K,N)=(AJM(I,M1,K)*F(I,M2,K,N)-TEMP+CON(I,M1,K))&
     &/(AP(I,M1,K)+small)
  160 FLUXM1(I,K,N)=AJM(I,M1,K)*(F(I,M1,K,N)-F(I,M2,K,N))+TEMP
      IF(KCY.NE.0) GO TO 175
      DO 170 J=JST,M2
      DO 170 K=KST,N2
      TEMP=AIM(ISTF,J,K)*(F(IST+1,J,K,N)-F(IST,J,K,N))
      IF(KBCI1(J,K).EQ.2)&
     & F(ISTF,J,K,N)=(AIP(ISTF,J,K)*F(IST,J,K,N)-TEMP+CON(ISTF,J,K))&
     & /(AP(ISTF,J,K)+small)
      FLUXI1(J,K,N)=AIP(ISTF,J,K)*(F(ISTF,J,K,N)-F(IST,J,K,N))+TEMP
      TEMP=AIP(L1,J,K)*(F(L3,J,K,N)-F(L2,J,K,N))
      IF(KBCL1(J,K).EQ.2)&
     & F(L1,J,K,N)=(AIM(L1,J,K)*F(L2,J,K,N)-TEMP+CON(L1,J,K))&
     &/(AP(L1,J,K)+small)
  170 FLUXL1(J,K,N)=AIM(L1,J,K)*(F(L1,J,K,N)-F(L2,J,K,N))+TEMP
  175 CONTINUE
!
!  REINICIALIZA: CON,AP,KBC,FLXC, Y FLXP
!-----------------------------------------------------------------------
      DO 180 K=2,N2
      DO 180 J=2,M2
      KBCI1(J,K)=1
      KBCL1(J,K)=1
      FLXCI1(J,K)=0.
      FLXCL1(J,K)=0.
      FLXPI1(J,K)=0.
      FLXPL1(J,K)=0.
      DO 180 I=2,L2
      CON(I,J,K)=0.
      AP(I,J,K)=0.
  180 CONTINUE
      DO 190 K=2,N2
      DO 190 I=2,L2
      KBCJ1(I,K)=1
      KBCM1(I,K)=1
      FLXCJ1(I,K)=0.
      FLXCM1(I,K)=0.
      FLXPJ1(I,K)=0.
      FLXPM1(I,K)=0.
  190 CONTINUE
      DO 195 J=2,M2
      DO 195 I=2,L2
      KBCK1(I,J)=1
      KBCN1(I,J)=1
      FLXCK1(I,J)=0.
      FLXCN1(I,J)=0.
      FLXPK1(I,J)=0.
      FLXPN1(I,J)=0.
  195 CONTINUE
      RETURN
      END
!>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
      SUBROUTINE TOOLS
!<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
      INCLUDE '3DCOMMON.F90'
!     =================================================================
      ENTRY EZGRID
!     ������������
!     CONSTRUYE LA MALLA EN LA DIRECCION X
      L1=NCVLX+2
      XU(2)=0.
      XU(L1)=XL
      L2=L1-1
      FCVLX=FLOAT(NCVLX)
      DO I=3,L2
         DD=FLOAT(I-2)/FCVLX
         IF(POWERX.GT.0.) THEN
           XU(I)=XL*DD**POWERX
         ELSE
           XU(I)=XL*(1.-(1.-DD)**(-POWERX))
         ENDIF
      ENDDO
!     CONSTRUYE LA MALLA EN LA DIRECCION Y
      M1=NCVLY+2
      YV(2)=0.
      YV(M1)=YL
      M2=M1-1
      FCVLY=FLOAT(NCVLY)
      DO J=3,M2
         DD=FLOAT(J-2)/FCVLY
         IF(POWERY.GT.0.) THEN
           YV(J)=YL*DD**POWERY
         ELSE
           YV(J)=YL*(1.-(1.-DD)**(-POWERY))
         ENDIF
      ENDDO
!     CONSTRUYE LA MALLA EN LA DIRECCION Z
      N1=NCVLZ+2
      ZW(2)=0.
      ZW(N1)=ZL
      N2=N1-1
      FCVLZ=FLOAT(NCVLZ)
      DO K=3,N2
         DD=FLOAT(K-2)/FCVLZ
         IF(POWERZ.GT.0.) THEN
           ZW(K)=ZL*DD**POWERZ
         ELSE
           ZW(K)=ZL*(1.-(1.-DD)**(-POWERZ))
         ENDIF
      ENDDO
      RETURN
!*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
      ENTRY ZGRID
!     ����������?
!     CONSTRUYE LA MALLA ZONA-POR-ZONA
!     CONSIDERA LA DIRECCION X
      XU(2)=0.
      I2=2
      DO NZ=1,NZX
         FCVLX=FLOAT(NCVX(NZ))
         ILAST=I2
         I1=ILAST+1
         I2=ILAST+NCVX(NZ)
         DO I=I1,I2
            DD=FLOAT(I-ILAST)/FCVLX
            IF(POWRX(NZ).GT.0) THEN
              XU(I)=XU(ILAST)+XZONE(NZ)*DD**POWRX(NZ)
            ELSE
              XU(I)=XU(ILAST)+XZONE(NZ)*(1.-(1.-DD)**(-POWRX(NZ)))
            ENDIF
         ENDDO
      ENDDO
      L1=I2
!     CONSIDERA LA DIRECCION Y
      YV(2)=0.
      J2=2
      DO NZ=1,NZY
         FCVLY=FLOAT(NCVY(NZ))
         JLAST=J2
         J1=JLAST+1
         J2=JLAST+NCVY(NZ)
         DO J=J1,J2
            DD=FLOAT(J-JLAST)/FCVLY
            IF(POWRY(NZ).GT.0) THEN
              YV(J)=YV(JLAST)+YZONE(NZ)*DD**POWRY(NZ)
            ELSE
              YV(J)=YV(JLAST)+YZONE(NZ)*(1.-(1.-DD)**(-POWRY(NZ)))
            ENDIF
         ENDDO
      ENDDO
      M1=J2
!     CONSIDERA LA DIRECCION Z
      ZW(2)=0.
      K2=2
      DO NZ=1,NZZ
         FCVLZ=FLOAT(NCVZ(NZ))
         KLAST=K2
         K1=KLAST+1
         K2=KLAST+NCVZ(NZ)
         DO K=K1,K2
            DD=FLOAT(K-KLAST)/FCVLZ
            IF(POWRZ(NZ).GT.0) THEN
              ZW(K)=ZW(KLAST)+ZZONE(NZ)*DD**POWRZ(NZ)
            ELSE
              ZW(K)=ZW(KLAST)+ZZONE(NZ)*(1.-(1.-DD)**(-POWRZ(NZ)))
            ENDIF
         ENDDO
      ENDDO
      N1=K2
      RETURN
!*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
      ENTRY PRINT
!     ����������?
!     PRESIONES POR EXTRAPOLACION
      IF(KPRINT(NP).EQ.1) THEN
!ONSTRUYE LAS PRESIONES DE CONTORNO POR EXTRAPOLACION
!ALCULO EN LA DIRECCION X
      DO K=2,N2
      DO J=2,M2
      P(1,J,K)=(P(2,J,K)*XCVS(3)-P(3,J,K)*XDIF(2))/XDIF(3)
      P(L1,J,K)=(P(L2,J,K)*XCVS(L2)-P(L3,J,K)*XDIF(L1))&
     & /XDIF(L2)
      ENDDO
      ENDDO
!ALCULO EN LA DIRECCION Y
      DO K=2,N2
      DO I=2,L2
      P(I,1,K)=(P(I,2,K)*YCVS(3)-P(I,3,K)*YDIF(2))/YDIF(3)
      P(I,M1,K)=(P(I,M2,K)*YCVS(M2)-P(I,M3,K)*YDIF(M1))&
     & /YDIF(M2)
      ENDDO
      ENDDO
!ALCULO EN LA DIRECCION Z
      DO J=2,M2
      DO I=2,L2
      P(I,J,1)=(P(I,J,2)*ZCVS(3)-P(I,J,3)*ZDIF(2))/ZDIF(3)
      P(I,J,N1)=(P(I,J,N2)*ZCVS(N2)-P(I,J,N3)*ZDIF(N1))&
     & /ZDIF(N2)
      ENDDO
      ENDDO
!ALCULO EN LAS ARISTAS PARA PRESION
!ALCULO EN LA DIRECCI? X
      DO I=2,L2
      P(I,1,1)=P(I,2,1)+P(I,1,2)-P(I,2,2)
      P(I,M1,1)=P(I,M2,1)+P(I,M1,2)-P(I,M2,2)
      P(I,1,N1)=P(I,1,N2)+P(I,2,N1)-P(I,2,N2)
      P(I,M1,N1)=P(I,M1,N2)+P(I,M2,N1)-P(I,M2,N2)
      END DO
!ALCULO EN LA DIRECCI? Y
      DO J=2,M2
      P(1,J,1)=P(2,J,1)+P(1,J,2)-P(2,J,2)
      P(L1,J,1)=P(L2,J,1)+P(L1,J,2)-P(L2,J,2)
      P(1,J,N1)=P(1,J,N2)+P(2,J,N1)-P(2,J,N2)
      P(L1,J,N1)=P(L1,J,N2)+P(L2,J,N1)-P(L2,J,N2)
      END DO
!ALCULO EN LA DIRECCI? Z
      DO K=2,N2
      P(1,1,K)=P(2,1,K)+P(1,2,K)-P(2,2,K)
      P(1,M1,K)=P(1,M2,K)+P(2,M1,K)-P(2,M2,K)
      P(L1,1,K)=P(L2,1,K)+P(L1,2,K)-P(L2,2,K)
      P(L1,M1,K)=P(L1,M2,K)+P(L2,M1,K)-P(L2,M2,K)
      END DO
!ALCULOS EN LAS PUNTAS
      P(1,1,1)=P(2,1,1)+P(1,2,1)+P(1,1,2)+P(2,2,2)&
     &       -(P(2,2,1)+P(1,2,2)+P(2,1,2))
      P(L1,1,1)=P(L2,1,1)+P(L1,2,1)+P(L1,1,2)+P(L2,2,2)&
     &        -(P(L2,1,2)+P(L2,2,1)+P(L1,2,2))
      P(1,M1,1)=P(2,M1,1)+P(1,M2,1)+P(1,M1,2)+P(2,M2,2)&
     &        -(P(2,M1,2)+P(1,M2,2)+P(2,M2,1))
      P(1,1,N1)=P(2,1,N1)+P(1,2,N1)+P(1,1,N2)+P(2,2,N2)&
     &        -(P(2,1,N2)+P(1,2,N2)+P(2,2,N1))
      P(L1,M1,1)=P(L2,M1,1)+P(L1,M2,1)+P(L1,M1,2)&
     &          +P(L2,M2,2)-(P(L1,M2,2)+P(L2,M2,1)+P(L2,M1,2))
      P(L1,1,N1)=P(L2,1,N1)+P(L1,2,N1)+P(L1,1,N2)&
     &          +P(L2,2,N2)-(P(L2,1,N2)+P(L1,2,N2)+P(L2,2,N1))
      P(L1,M1,N1)=P(L2,M1,N1)+P(L1,M2,N1)+P(L1,M1,N2)&
     &           +P(L2,M2,N2)-(P(L2,M1,N2)+P(L2,M2,N1)+P(L1,M2,N2))
      P(1,M1,N1)=P(2,M1,N1)+P(1,M2,N1)+P(1,M1,N2)&
     &          +P(2,M2,N2)-(P(2,M1,N2)+P(2,M2,N1)+P(1,M2,N2))
!     OBTENCION DE VALORES DE PRESION RESPECTO AL PUNTO (1,1,1)
      PREF=P(1,1,1)
      DO K=1,N1
      DO J=1,M1
      DO I=1,L1
         P(I,J,K)=P(I,J,K)-PREF
      ENDDO
      ENDDO
      ENDDO
      ENDIF
!++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
!     VALORES POR EXTRAPOLACION EN LAS ARISTAS
      DO N=5,NFMAX
         NF=N
         IF(KPRINT(NF).EQ.1) THEN
           IF (IBORX(NF).EQ.1) THEN
!ALCULO EN LA DIRECCI? X
           DO I=2,L2
              F(I,1,1,NF)=F(I,2,1,NF)+F(I,1,2,NF)-F(I,2,2,NF)
              F(I,M1,1,NF)=F(I,M2,1,NF)+F(I,M1,2,NF)-F(I,M2,2,NF)
              F(I,1,N1,NF)=F(I,1,N2,NF)+F(I,2,N1,NF)-F(I,2,N2,NF)
              F(I,M1,N1,NF)=F(I,M1,N2,NF)+F(I,M2,N1,NF)-F(I,M2,N2,NF)
           END DO
           ENDIF
           IF (IBORY(NF).EQ.1) THEN
!ALCULO EN LA DIRECCI? Y
           DO J=2,M2
           F(1,J,1,NF)=F(2,J,1,NF)+F(1,J,2,NF)-F(2,J,2,NF)
           F(L1,J,1,NF)=F(L2,J,1,NF)+F(L1,J,2,NF)-F(L2,J,2,NF)
           F(1,J,N1,NF)=F(1,J,N2,NF)+F(2,J,N1,NF)-F(2,J,N2,NF)
           F(L1,J,N1,NF)=F(L1,J,N2,NF)+F(L2,J,N1,NF)-F(L2,J,N2,NF)
           END DO
           ENDIF
           IF (IBORZ(NF).EQ.1) THEN
!ALCULO EN LA DIRECCI? Z
           DO K=2,N2
           F(1,1,K,NF)=F(2,1,K,NF)+F(1,2,K,NF)-F(2,2,K,NF)
           F(1,M1,K,NF)=F(1,M2,K,NF)+F(2,M1,K,NF)-F(2,M2,K,NF)
           F(L1,1,K,NF)=F(L2,1,K,NF)+F(L1,2,K,NF)-F(L2,2,K,NF)
           F(L1,M1,K,NF)=F(L1,M2,K,NF)+F(L2,M1,K,NF)-F(L2,M2,K,NF)
           END DO
           ENDIF
          IF (IPUN(NF).EQ.1) THEN
!ALCULOS EN LAS PUNTAS
      F(1,1,1,NF)=F(2,1,1,NF)+F(1,2,1,NF)+F(1,1,2,NF)+F(2,2,2,NF)&
     &          -(F(2,2,1,NF)+F(1,2,2,NF)+F(2,1,2,NF))
      F(L1,1,1,NF)=F(L2,1,1,NF)+F(L1,2,1,NF)+F(L1,1,2,NF)+F(L2,2,2,NF)&
     &          -(F(L2,1,2,NF)+F(L2,2,1,NF)+F(L1,2,2,NF))
      F(1,M1,1,NF)=F(2,M1,1,NF)+F(1,M2,1,NF)+F(1,M1,2,NF)+F(2,M2,2,NF)&
     &          -(F(2,M1,2,NF)+F(1,M2,2,NF)+F(2,M2,1,NF))
      F(1,1,N1,NF)=F(2,1,N1,NF)+F(1,2,N1,NF)+F(1,1,N2,NF)+F(2,2,N2,NF)&
     &          -(F(2,1,N2,NF)+F(1,2,N2,NF)+F(2,2,N1,NF))
      F(L1,M1,1,NF)=F(L2,M1,1,NF)+F(L1,M2,1,NF)+F(L1,M1,2,NF)&
     &    +F(L2,M2,2,NF)-(F(L1,M2,2,NF)+F(L2,M2,1,NF)+F(L2,M1,2,NF))
      F(L1,1,N1,NF)=F(L2,1,N1,NF)+F(L1,2,N1,NF)+F(L1,1,N2,NF)&
     &    +F(L2,2,N2,NF)-(F(L2,1,N2,NF)+F(L1,2,N2,NF)+F(L2,2,N1,NF))
      F(L1,M1,N1,NF)=F(L2,M1,N1,NF)+F(L1,M2,N1,NF)+F(L1,M1,N2,NF)&
     &    +F(L2,M2,N2,NF)-(F(L2,M1,N2,NF)+F(L2,M2,N1,NF)+F(L1,M2,N2,NF))
      F(1,M1,N1,NF)=F(2,M1,N1,NF)+F(1,M2,N1,NF)+F(1,M1,N2,NF)&
     &    +F(2,M2,N2,NF)-(F(2,M1,N2,NF)+F(2,M2,N1,NF)+F(1,M2,N2,NF))
          ENDIF
         ENDIF
      ENDDO
!+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      IF(KEPR.EQ.0) THEN
        DO IUNIT=IU1,IU2
!          ARREGLA LA SALIDA DEL CAMPO TRI-DIMENSIONAL
           IF(KPGR.NE.0.AND.NPTI.EQ.IPTM) THEN
!            CREA SALIDA PARA LA MALLA
             WRITE(IUNIT,1)
    1        FORMAT(' ')
             IBEG=1
             IEND=L1
             IREP=(IEND-IBEG+7)/7
             DO KG=1,IREP
                INCR=MIN(6,IEND-IBEG)
                ISTOP=IBEG+INCR
                WRITE(IUNIT,2) (I,I=IBEG,ISTOP)
    2           FORMAT(/2X,'I =',2X,7(I4,5X))
                IF(MODE.EQ.2) THEN
                  WRITE(IUNIT,3) (X(I),I=IBEG,ISTOP)
    3             FORMAT(1X,'TH =',1P7E9.2)
                ELSE
                  WRITE(IUNIT,4) (X(I),I=IBEG,ISTOP)
    4             FORMAT(2X,'X =',1P7E9.2)
                ENDIF
                IBEG=ISTOP+1
             ENDDO
!
             JBEG=1
             JEND=M1
             JREP=(JEND-JBEG+7)/7
             DO KG=1,JREP
                INCR=MIN(6,JEND-JBEG)
                JSTOP=JBEG+INCR
                WRITE(IUNIT,5) (J,J=JBEG,JSTOP)
    5           FORMAT(/2X,'J =',2X,7(I4,5X))
                WRITE(IUNIT,6) (Y(J),J=JBEG,JSTOP)
    6           FORMAT(2X,'Y =',1P7E9.2)
                JBEG=JSTOP+1
             ENDDO
!
             WRITE(IUNIT,1)
             KBEG=1
             KEND=N1
             KREP=(KEND-KBEG+7)/7
             DO KG=1,KREP
                INCR=MIN(6,KEND-KBEG)
                KSTO=KBEG+INCR
                WRITE(IUNIT,11) (K,K=KBEG,KSTO)
   11           FORMAT(/2X,'K =',2X,7(I4,5X))
                WRITE(IUNIT,12) (Z(K),K=KBEG,KSTO)
   12           FORMAT(2X,'Z =',1P7E9.2)
                KBEG=KSTO+1
             ENDDO
           ENDIF
!     CREA SALIDA PARA LOS VALORES DE LAS VARIABLES DEPENDIENTES
           DO N=1,NP
              NF=N
              IF(KPRINT(NF).NE.0) THEN
!             PRESENTACION DE RESULTADOS EN PLANOS EN 'Z'
              IF(IXYZ(NF).EQ.3) THEN
                WRITE(IUNIT,7) TITLE(NF)
    7           FORMAT(/1X,6(1H*),3X,A18,3X,6(1H*)/9X,20(1H-))
                KB=1
                KE=N1
                IF(NF.LT.5) KB=2
                DO K=KB,KE
                   WRITE(IUNIT,13) K
   13              FORMAT(/'  K =',I2)
                   IBEG=1
                   JBEG=1
                   IEND=L1
                   JEND=M1
                   IF(KCY.NE.0) THEN
                     IBEG=2
                     IF(NF.EQ.1) IBEG=3
                     IEND=L2
                   ENDIF
                   IF(NF.LT.5) THEN
                    IBEG=2; JBEG=2
                   ENDIF
                   IREP=(IEND-IBEG+7)/7
                   DO KG=1,IREP
                      INCR=MIN(6,IEND-IBEG)
                      ISTOP=IBEG+INCR
                      WRITE(IUNIT,8) (I,I=IBEG,ISTOP)
    8                 FORMAT(/'  I =',I6,6I9)
                      WRITE(IUNIT,9)
    9                 FORMAT('  J')
                      DO J=JEND,JBEG,-1
                         WRITE(IUNIT,10) J,(F(I,J,K,NF),I=IBEG,ISTOP)
   10                    FORMAT(1X,I2,3X,1P7E9.2)
                      ENDDO
                      IBEG=ISTOP+1
                   ENDDO
                ENDDO
              ENDIF
!             PRESENTACION DE RESULTADOS EN PLANOS EN 'X'
              IF(IXYZ(NF).EQ.1) THEN
                WRITE(IUNIT,17) TITLE(NF)
   17           FORMAT(/1X,6(1H*),3X,A18,3X,6(1H*)/9X,20(1H-))
                IB=1
                IE=L1
                IF(KCY.NE.0) THEN
                  IB=2
                    IF(NF.EQ.1) IB=3
                  IE=L2
                ENDIF
                IF(NF.LT.5) IB=2
                DO I=IB,IE
                   WRITE(IUNIT,23) I
   23              FORMAT(/'  I =',I2)
                   KBEG=1
                   JBEG=1
                   KEND=N1
                   JEND=M1
                   IF(NF.LT.5) THEN
                     JBEG=2; KBEG=2
                   ENDIF
                   KREP=(KEND-KBEG+7)/7
                   DO KG=1,KREP
                      INCR=MIN(6,KEND-KBEG)
                      KSTOP=KBEG+INCR
                      WRITE(IUNIT,18) (K,K=KBEG,KSTOP)
   18                 FORMAT(/'  K =',I6,6I9)
                      WRITE(IUNIT,19)
   19                 FORMAT('  J')
                      DO J=JEND,JBEG,-1
                         WRITE(IUNIT,31) J,(F(I,J,K,NF),K=KBEG,KSTOP)
   31                    FORMAT(1X,I2,3X,1P7E9.2)
                      ENDDO
                      KBEG=KSTOP+1
                   ENDDO
                ENDDO
                ENDIF
!               PRESENTACION DE RESULTADOS EN PLANOS O SUPERFICIES EN 'Y
                IF(IXYZ(NF).EQ.2) THEN
                WRITE(IUNIT,27) TITLE(NF)
   27           FORMAT(/1X,6(1H*),3X,A18,3X,6(1H*)/9X,20(1H-))
                JB=1
                JE=M1
                IF(NF.LT.5) JB=2
                DO J=JB,JE
                   WRITE(IUNIT,33) J
   33              FORMAT(/'  J =',I2)
                   IBEG=1
                   KBEG=1
                   IEND=L1
                   KEND=N1
                   IF(KCY.NE.0) THEN
                     IBEG=2
                     IF(NF.EQ.1) IBEG=3
                     IEND=L2
                   ENDIF
                   IF(NF.LT.5) THEN
                    IBEG=2; KBEG=2
                   ENDIF
                   IREP=(IEND-IBEG+7)/7
                   DO KG=1,IREP
                      INCR=MIN(6,IEND-IBEG)
                      ISTOP=IBEG+INCR
                      WRITE(IUNIT,28) (I,I=IBEG,ISTOP)
   28                 FORMAT(/'  I =',I6,6I9)
                      WRITE(IUNIT,29)
   29                 FORMAT('  K')
                      DO K=KEND,KBEG,-1
                         WRITE(IUNIT,41) K,(F(I,J,K,NF),I=IBEG,ISTOP)
   41                    FORMAT(1X,I2,3X,1P7E9.2)
                      ENDDO
                      IBEG=ISTOP+1
                   ENDDO
                ENDDO
                ENDIF
              ENDIF
           ENDDO
        ENDDO
      ENDIF
      RETURN
      END
!>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
      SUBROUTINE DIFLOW
!<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
      INCLUDE '3DCOMMON.F90'
!     =================================================================
      ACOF=DIFF
      IF(FLOW.EQ.0.)RETURN
      TEMP=DIFF-ABS(FLOW)*0.1
      ACOF=0.
      IF(TEMP.LE.0.)RETURN
      TEMP=TEMP/DIFF
      ACOF=DIFF*TEMP**5
      RETURN
      END
!>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
      SUBROUTINE PLOT
!<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
      INCLUDE '3DCOMMON.F90'
!     =================================================================
      OPEN(UNIT=8,FILE=PLOTF)
      IF(MODE.EQ.2.AND.KCY.NE.0) THEN
        DO K=1,N1
         DO J=1,M1
           ALGA=XDIF(2)/(XDIF(2)+XDIF(L1))*(V(L2,J,K)-V(2,J,K))+V(2,J,K)
           V(1,J,K)=ALGA
           V(L1,J,K)=ALGA
         ENDDO
        ENDDO
        DO K=1,N1
         DO J=1,M1
           ALTA=XDIF(2)/(XDIF(2)+XDIF(L1))*(W(L2,J,K)-W(2,J,K))+W(2,J,K)
           W(1,J,K)=ALTA
           W(L1,J,K)=ALTA
         ENDDO
        ENDDO
        DIST=XDIF(2)+XDIF(3)+XDIF(L1)
        DO K=1,N1
         DO J=1,M1
            ALFA1=(XDIF(2)+XDIF(3))/DIST*(U(L2,J,K)-U(3,J,K))+U(3,J,K)
            U(1,J,K)=ALFA1
            U(L1,J,K)=ALFA1
            ALFA2=XDIF(3)/DIST*(U(L2,J,K)-U(3,J,K))+U(3,J,K)
            U(2,J,K)=ALFA2
          ENDDO
        ENDDO
        DO K=1,N1
          DO J=1,M1
            DO I=1,L1
               W(I,1,K)=W(I,2,K)
               U(I,1,K)=U(I,2,K)
            ENDDO
          ENDDO
        ENDDO
      DO K=1,N1
       DO J=1,M1
          ALFAX=XDIF(2)/(XDIF(2)+XDIF(L1))*(T(L2,J,K)-T(2,J,K))+T(2,J,K)
          T(1,J,K)=ALFAX
          T(L1,J,K)=ALFAX
        ENDDO
       ENDDO
      ENDIF
!     CREA ARCHIVO DE DATOS PARA GRAFICAR
      WRITE(8,300) HEADER
  300 FORMAT(1X,'TITLE = " ',A64,'"')
      WRITE(8,*)'VARIABLES = "X(m)"'
      WRITE(8,*)'"Y(m)"'
      WRITE(8,*)'"Z(m)"'
      DO N=1,NP
	 WRITE(8,400)TITLE(N)
  400    FORMAT('"',A8,'"')
      ENDDO
	WRITE(8,500) L1,M1,N1
  500 FORMAT('ZONE TITLES =  ZONA1,  I=',I3,3X,'J=',I3,3X,'K=',I3)
	WRITE(8,*)'C=WHITE, F=POINT,'
      DO K=1,N1
        DO J=1,M1
          DO I=1,L1
             XI=X(I)
             YJ=Y(J)
             IF (MODE.EQ.2) THEN
                XI=R(J)*SIN(X(I))
                YJ=R(J)*COS(X(I))
             ENDIF
             WRITE(8,'(15e13.4)') XI,YJ,Z(K),(F(I,J,K,N),N=1,NP)
          END DO
        END DO
      END DO
!     CREA LA DATA PARA GRAFICAR EN TECPLOT
      CLOSE(8)
      RETURN
      END
!>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
      SUBROUTINE COPRES
!<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
      INCLUDE '3DCOMMON.F90'
!     =================================================================
!----------------------------------------------------------------------
!OEFICIENTES PARA LA ECUACION DE CORRECCION DE PRESION P'
!----------------------------------------------------------------------
      NF=4
      IF(KSOLVE(NF).EQ.0) GO TO 100
      IST=2
      JST=2
      KST=2
      CALL PHI
      SMAX=0.
      SSUM=0.
!ONSIDERA LOS TERMINOS VOLUMETRICOS
      DO K=2,N2
        DO J=2,M2
          DO I=2,L2
             VOL=XCV(I)*YCVR(J)*ZCV(K)
             CON(I,J,K)=CON(I,J,K)*VOL
          ENDDO
        ENDDO
      ENDDO
!ALCULO DE LOS COEFICIENTES EN LA DIRECCION X
      LEND=L3
      IF(KCY.NE.0) LEND=L2
      DO K=2,N2
        DO J=2,M2
          DO I=2,LEND
             IFOR=I+1
             IF(I.EQ.L2) IFOR=2
             ARHO=ARX(J,K)*(FX(IFOR)*RHO(IFOR,J,K)&
     &            +FXM(IFOR)*RHO(I,J,K))
             FLOW=ARHO*F(IFOR,J,K,1)
             CON(I,J,K)=CON(I,J,K)-FLOW
             CON(IFOR,J,K)=CON(IFOR,J,K)+FLOW
             AIP(I,J,K)=ARHO*DU(IFOR,J,K)
             AIM(IFOR,J,K)=AIP(I,J,K)
          ENDDO
        ENDDO
      ENDDO
      IF(KCY.NE.0) GO TO 110
!ONSIDERA EL PLANO I=1
      DO K=2,N2
        DO J=2,M2
           ARHO=ARX(J,K)*RHO(1,J,K)
           CON(2,J,K)=CON(2,J,K)+ARHO*F(2,J,K,1)
           AIM(2,J,K)=0.
!ONSIDERA EL PLANO I=L1
           ARHO=ARX(J,K)*RHO(L1,J,K)
           CON(L2,J,K)=CON(L2,J,K)-ARHO*F(L1,J,K,1)
           AIP(L2,J,K)=0.
        ENDDO
      ENDDO
  110 CONTINUE
!ALCULO DE LOS COEFICIENTES EN LA DIRECCION Y
      DO K=2,N2
        DO J=2,M3
          DO I=2,L2
             ARHO=RV(J+1)*XCV(I)*ZCV(K)*(FY(J+1)*RHO(I,J+1,K)&
     &            +FYM(J+1)*RHO(I,J,K))
             FLOW=ARHO*F(I,J+1,K,2)
             CON(I,J,K)=CON(I,J,K)-FLOW
             CON(I,J+1,K)=CON(I,J+1,K)+FLOW
             AJP(I,J,K)=ARHO*DV(I,J+1,K)
             AJM(I,J+1,K)=AJP(I,J,K)
          ENDDO
        ENDDO
      ENDDO
!ONSIDERA EL PLANO J=1
      DO K=2,N2
        DO I=2,L2
           ARHO=R(1)*XCV(I)*ZCV(K)*RHO(I,1,K)
           CON(I,2,K)=CON(I,2,K)+ARHO*F(I,2,K,2)
           AJM(I,2,K)=0.
!ONSIDERA EL PLANO J=M1
           ARHO=RV(M1)*XCV(I)*ZCV(K)*RHO(I,M1,K)
           CON(I,M2,K)=CON(I,M2,K)-ARHO*F(I,M1,K,2)
           AJP(I,M2,K)=0.
        ENDDO
      ENDDO
!ALCULO DE LOS COEFICIENTES EN LA DIRECCION Z
      DO K=2,N3
        DO J=2,M2
          DO I=2,L2
             ARHO=ARZ(I,J)*(FZ(K+1)*RHO(I,J,K+1)+FZM(K+1)*RHO(I,J,K))
             FLOW=ARHO*F(I,J,K+1,3)
             CON(I,J,K)=CON(I,J,K)-FLOW
             CON(I,J,K+1)=CON(I,J,K+1)+FLOW
             AKP(I,J,K)=ARHO*DW(I,J,K+1)
             AKM(I,J,K+1)=AKP(I,J,K)
          ENDDO
        ENDDO
      ENDDO
!ONSIDERA EL PLANO K=1
      DO J=2,M2
        DO I=2,L2
           ARHO=ARZ(I,J)*RHO(I,J,1)
           CON(I,J,2)=CON(I,J,2)+ARHO*F(I,J,2,3)
           AKM(I,J,2)=0.
!ONSIDERA EL PLANO K=N1
           ARHO=ARZ(I,J)*RHO(I,J,N1)
           CON(I,J,N2)=CON(I,J,N2)-ARHO*F(I,J,N1,3)
           AKP(I,J,N2)=0.
        ENDDO
      ENDDO
!OMIENZA AQUI A BALANCEAR LAS FUENTES DE MASA
!ONSTRUYE A AP(I,J,K) y CON(I,J,K) EN SU FORMA FINAL
      DO K=2,N2
        DO J=2,M2
          DO I=2,L2
             AP(I,J,K)=AIP(I,J,K)+AIM(I,J,K)+AJP(I,J,K)+AJM(I,J,K)&
     &                                      +AKP(I,J,K)+AKM(I,J,K)
             F(I,J,K,4)=0.
             SMAX=MAX(SMAX,ABS(CON(I,J,K)))
             SSUM=SSUM+CON(I,J,K)
          ENDDO
        ENDDO
      ENDDO
      CALL SOLVE
!OMIENZA AQUI A CORREGIR LA PRESION Y LAS VELOCIDADES
      DO K=2,N2
        DO J=2,M2
          DO I=2,L2
             P(I,J,K)=P(I,J,K)+F(I,J,K,4)*RELAX(NP)
             IF(I.NE.2) F(I,J,K,1)=F(I,J,K,1)+DU(I,J,K)*(F(I-1,J,K,4)&
     &                                                  -F(I,J,K,4))
             IF(J.NE.2) F(I,J,K,2)=F(I,J,K,2)+DV(I,J,K)*(F(I,J-1,K,4)&
     &                                                  -F(I,J,K,4))
             IF(K.NE.2) F(I,J,K,3)=F(I,J,K,3)+DW(I,J,K)*(F(I,J,K-1,4)&
     &                                                  -F(I,J,K,4))
          ENDDO
        ENDDO
      ENDDO
  100 RETURN
      END

