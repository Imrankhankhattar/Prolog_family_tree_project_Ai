%implementing mianbiwi logic

mianbiwi(chotekhan,chotirani).
mianbiwi(barrekhan,barrirani).
mianbiwi(salim,kauser).
mianbiwi(nadir,nahid).
mianbiwi(asad,sumra).
mianbiwi(rizwan,sanam).

%implementing gins logic
%mards
gins(mard,chotekhan).
gins(mard,barrekhan).
gins(mard,salim).
gins(mard,nadir).
gins(mard,asad).
gins(mard,rizwan).
gins(mard,burhan).
gins(mard,rashid).
gins(mard,akram).
%aurats
gins(aurat,chotirani).
gins(aurat,barrirani).
gins(aurat,kauser).
gins(aurat,nahid).
gins(aurat,sumra).
gins(aurat,sanam).
gins(aurat,salima).
gins(aurat,rabia).

%implementing parents logic
parents(chotekhan,kauser).
parents(chotekhan,nadir).
parents(chotekhan,asad).
parents(chotirani,kauser).
parents(chotirani,nadir).
parents(chotirani,asad).
parents(barrekhan,nahid).
parents(barrekhan,sumra).
parents(barrirani,nahid).
parents(barrirani,sumra).
parents(salim,rizwan).
parents(kauser,rizwan).
parents(nadir,burhan).
parents(nadir,rashid).
parents(nadir,akram).
parents(nahid,burhan).
parents(nahid,rashid).
parents(nahid,akram).
parents(asad,salima).
parents(asad,sanam).
parents(sumra,salima).
parents(sumra,sanam).
parents(rizwan,rabia).
parents(sanam,rabia).


%implementing baap rule
baap(X,Y):- parents(X,Y), gins(mard,X).

%implementing maa rule
maa(X,Y) :- parents(X,Y), gins(aurat,X).

%implementing beta rule
beta(X,Y):- parents(Y,X), gins(mard,X).

%implementing beti rule
beti(X,Y):- parents(Y,X), gins(aurat,X).

%implementing dada rule
dada(X,Y):- parents(X,Z), parents(Z,Y),gins(mard,Z),gins(mard,X).

%implementing dadi rule
dadi(X,Y):- parents(X,Z), parents(Z,Y),gins(mard,Z),gins(aurat,X).

%implementing nana rule
nana(X,Y):- parents(X,Z), parents(Z,Y),gins(aurat,Z),gins(mard,X).

%implementing nana rule
nani(X,Y):- parents(X,Z), parents(Z,Y),gins(aurat,Z),gins(aurat,X).

%implementing sala rule
sala(X,Y):- mianbiwi(Y,Z),parents(B,Z),gins(mard,B),beta(X,B),gins(mard,X).

%implementing sali rule
sali(X,Y):- mianbiwi(Y,Z),parents(B,Z),gins(mard,B),beta(X,B),gins(aurat,X).

%implementing bahu rule
bahu(X,Y) :- mianbiwi(Z,X),parents(Y,Z).

%implementing damad rule
damad(X,Y) :- mianbiwi(X,Z),parents(Y,Z).

%emplementing pota rule
pota(X,Y):- parents(Y,Z),gins(mard,Z),parents(Z,X),gins(mard,X).

%emplementing poti rule
poti(X,Y):- parents(Y,Z),gins(mard,Z),parents(Z,X),gins(aurat,X).

%emplementing nawasa rule
nawasa(X,Y):- parents(Y,Z),gins(aurat,Z),parents(Z,X),gins(mard,X).

%emplementing nawasi rule
nawasi(X,Y):- parents(Y,Z),gins(aurat,Z),parents(Z,X),gins(aurat,X).

%emplementing sussar rule
sassur(X,Y):- mianbiwi(Y,Z),parents(X,Z),gins(mard,X).
sassur(X,Y):- mianbiwi(Z,Y),parents(X,Z),gins(mard,X).

%emplementing chachataya rule
chachataya(X,Y):- pota(Y,D),gins(mard,D),beta(X,D),not(baap(X,Y)),gins(mard,X).

%emplementing khala rule
khala(X,Y):- nawasa(Y,D),gins(aurat,D),beti(X,D),not(maa(X,Y)),gins(aurat,X).
khala(X,Y):- nawasi(Y,D),gins(aurat,D),beti(X,D),not(maa(X,Y)),gins(aurat,X).

%emplementing baapdada rule
baapdada(X,Y) :- parents(X,Y),gins(mard,X).
baapdada(X,Y) :- parents(X,Z),gins(mard,X),baapdada(Z,Y).







































