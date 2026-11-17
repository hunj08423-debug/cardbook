# 글자 그림 카드 128장 가운데 그림을 찾은 카드들 (2026-11-17)
#  - 모두 위키미디어 공용의 퍼블릭 도메인·CC 그림이에요. 라이선스는 위키미디어 API로 하나씩 확인했어요.
#  - 영화·게임·책처럼 저작권이 있는 작품은 그 장면 대신 촬영지나 바탕이 된 옛 그림을 넣고,
#    캡션에 '○○ 장면이 아니라 △△예요'라고 밝혀요. 인물 사진은 넣지 않아요(그림·조각·장소는 됨).
#  - 칸: (카드 id, 위키미디어 파일 이름, 쪽(PDF·DjVu만), 카드에서 보일 자리 [가로%, 세로%], 캡션(cr), 그림 설명(alt))
FIX = [
# 10장 화면과 놀이
('jf-nazareth', 'Ribat_-_Monastir_-_03.jpg', None, [8, 60], '드라마 장면이 아니라, 1세기 예루살렘 역할을 한 튀니지 도시 모나스티르의 옛 요새(리바트)예요 · 사진: Wissem Miri · CC BY-SA 4.0 · 위키미디어 공용', '튀니지 모나스티르의 리바트. 누런 돌로 쌓은 성벽과 높은 탑이 있는 바닷가 요새.'),
('jf-jesusfilm', 'Sea-of-Galilee-1900.jpg', None, [50, 55], '영화 장면이 아니라, 영화를 찍은 땅 이스라엘의 갈릴래아 호수예요(1900년 무렵 사진) · 사진: 작자 미상 · 퍼블릭 도메인 · 위키미디어 공용', '갈릴래아 호수. 잔잔한 물 위에 돛단배가 떠 있고 멀리 언덕이 보이는 옛 컬러 사진.'),
('jf-passion', 'Rioni_Sassi_di_Matera_-_panoramio.jpg', None, [50, 50], '영화 장면이 아니라, 영화를 찍은 이탈리아 마테라의 옛 동굴 마을 ‘사시’예요 · 사진: Art Anderson · CC BY-SA 3.0 · 위키미디어 공용', '마테라의 사시. 바위 언덕을 따라 돌집이 층층이 쌓인 옛 마을.'),
('jf-chosen', 'Ancient_Boat_of_Sea_of_Galilee.jpg', None, [50, 50], '드라마 장면이 아니라, 1986년 갈릴래아 호숫가에서 찾은 2천 년 전 고깃배예요. 제자 어부들이 탔을 법한 배예요 · 사진: Warfieldian · CC BY-SA 4.0 · 위키미디어 공용', '갈릴래아 배. 박물관 안 쇠틀 위에 놓인, 나무판이 드러난 옛 고깃배의 뼈대.'),
('jf-benhur', 'Jean_Léon_Gérôme_-_Chariot_Race_-_1983.380_-_Art_Institute_of_Chicago.jpg', None, [70, 50], '영화 장면이 아니라, 로마의 전차 경주를 그린 장레옹 제롬의 그림(1876)이에요 · 그림: 장레옹 제롬 「전차 경주」, 시카고 미술관 · 퍼블릭 도메인 · 위키미디어 공용', '로마 원형 경기장에서 말이 끄는 전차들이 흙먼지를 일으키며 달리는 그림.'),
('cl-silence', 'La_Grande_Chartreuse.JPG', None, [50, 50], '영화 장면이 아니라, 영화를 찍은 프랑스 알프스의 그랑드 샤르트뢰즈 수도원이에요 · 사진: Floriel · CC BY 2.5 · 위키미디어 공용', '숲으로 둘러싸인 산골짜기에 회색 지붕의 수도원 건물들이 모여 있는 모습.'),
('cl-gods', 'Monastère_de_Tibhirine_vue_des_champs.jpg', None, [5, 50], '영화 장면이 아니라, 이야기의 실제 장소인 알제리 티비린 수도원이에요(영화는 모로코에서 찍었어요) · 사진: Ps2613 · CC BY-SA 3.0 · 위키미디어 공용', '들판 너머 나무들 사이로 보이는 티비린 수도원 건물.'),
('cl-sisteract', "St_Paul's_Catholic_Church_(San_Francisco)_(2).jpg", None, [50, 45], '영화 장면이 아니라, 영화 속 성당으로 나온 샌프란시스코 성 바오로 성당이에요 · 사진: Chris06 · CC BY-SA 4.0 · 위키미디어 공용', '두 개의 뾰족한 탑이 솟은 회색 돌 성당.'),
('cl-twopopes', 'Palais_pontifical_de_Castel_Gandolfo.JPG', None, [50, 50], '영화 장면이 아니라, 영화에서 두 사람이 만나는 곳으로 그려진 카스텔간돌포 교황 궁이에요 · 사진: LPLT · CC BY-SA 4.0 · 위키미디어 공용', '광장에 면한 크림색 궁전 건물의 정면.'),
('cl-conclave', 'Fumata_bianca_-_Conclave_2025.jpg', None, [50, 50], '영화 장면이 아니라, 새 교황이 뽑혔음을 알리는 시스티나 성당 굴뚝의 흰 연기예요(2025년 5월 8일) · 사진: P 1997 · CC BY-SA 4.0 · 위키미디어 공용', '지붕 위 가는 굴뚝에서 흰 연기가 피어오르는 모습.'),
('tf-hacksaw', '20190406_Hacksaw_Ridge_rock_formation-1.jpg', None, [50, 50], '영화 장면이 아니라, 오키나와에 남아 있는 ‘핵소 고지’(마에다 절벽)의 바위예요 · 사진: Balon Greyjoy · CC0 · 위키미디어 공용', '풀과 나무에 덮인 가파른 회색 바위 봉우리.'),
('tf-amazing', 'Wedgwood_-_Anti-Slavery_Medallion_-_Walters_482597.jpg', None, [50, 50], '영화 장면이 아니라, 노예무역 폐지 운동의 상징이 된 웨지우드의 메달(1787년 무렵)이에요 · 자료: 조사이어 웨지우드, 월터스 미술관 · 퍼블릭 도메인 · 위키미디어 공용', '흰 바탕에 쇠사슬에 묶인 채 무릎 꿇은 사람을 검게 새긴 둥근 메달.'),
('tf-selma', 'The_Edmund_Pettus_Bridge_07312v.jpg', None, [50, 50], '영화 장면이 아니라, ‘피의 일요일’이 일어난 앨라배마주 셀마의 에드먼드 페터스 다리예요 · 사진: 캐럴 M. 하이스미스 · 퍼블릭 도메인 · 위키미디어 공용', '강 위에 놓인 회색 철제 아치 다리.'),
('tf-bonhoeffer', 'London_UK_Sculptures-at-Westminster-Abbey-Westgate-Bonhoeffer-01.jpg', None, [50, 45], '영화 장면이 아니라, 런던 웨스트민스터 사원 서쪽 문 위에 선 본회퍼의 조각이에요. 20세기 순교자 열 사람 가운데 한 사람이에요 · 사진: CEphoto, Uwe Aranas · CC BY-SA 3.0 · 위키미디어 공용', '고딕 벽감 안에 서 있는 본회퍼의 돌 조각.'),
('tf-mansent', 'Tumen_River_Winter.jpg', None, [50, 50], '영화 장면이 아니라, 북한과 중국 사이를 흐르는 겨울 두만강이에요(중국 쪽에서 찍은 사진) · 사진: Farm · CC BY-SA 3.0 · 위키미디어 공용', '얼어붙은 강 너머로 낮은 산이 보이는 겨울 풍경.'),
('gr-miryang', 'Yeongnamru_Miryang_Gyeongsangnamdo.JPG', None, [50, 50], '영화 장면이 아니라, 영화의 무대이자 촬영지인 경남 밀양의 영남루예요 · 사진: Maru4u · CC BY-SA 3.0 · 위키미디어 공용', '기와지붕을 얹은 옛 누각.'),
('gr-babette', 'Michael_Ancher_-_Vil_han_klare_pynten_-_1885.png', None, [50, 50], '영화 장면이 아니라, 19세기 덴마크 유틀란트 바닷가 어촌을 그린 미카엘 안케르의 그림(1885)이에요 · 그림: 미카엘 안케르 「그가 곶을 돌아올 수 있을까」 · 퍼블릭 도메인 · 위키미디어 공용', '바닷가에 모여 선 어부들이 거친 바다를 바라보는 그림.'),
('gr-imagine', 'Paradiso_Canto_31_(no_caption).jpg', None, [50, 40], '영화 장면이 아니라, 하늘의 가장 높은 곳을 그린 귀스타브 도레의 『신곡』 「천국」 편 판화예요 · 그림: 귀스타브 도레 · 퍼블릭 도메인 · 위키미디어 공용', '빛나는 하늘 한가운데로 천사들이 둥글게 겹겹이 모인 흑백 판화.'),
('gr-rublev', "Rublev's_saviour.jpg", None, [50, 35], '영화 장면이 아니라, 안드레이 루블료프가 그렸다고 전하는 「구세주」 이콘(15세기 초)이에요 · 그림: 안드레이 루블료프, 트레티야코프 미술관 · 퍼블릭 도메인 · 위키미디어 공용', '물감이 많이 벗겨진 나무판에 그린 그리스도의 얼굴 이콘.'),
('gr-gilead', 'Tabor_Congregational_Church.jpg', None, [50, 50], '책 표지가 아니라, 소설 속 마을 길리아드의 바탕이 된 아이오와주 타보르의 회중교회예요 · 사진: Jim Roberts · CC BY-SA 4.0 · 위키미디어 공용', '작은 종탑이 있는 시골 교회 건물.'),
('ff-giants', 'Downtown_Albany,_GA.jpg', None, [50, 50], '영화 장면이 아니라, 영화를 만든 셔우드 침례교회가 있는 조지아주 올버니 시내예요 · 사진: Khtexg98537(영어 위키백과) · CC BY-SA 3.0 · 위키미디어 공용', '낮은 건물이 늘어선 미국 소도시의 큰길.'),
('ff-notdead', 'Die_fröhliche_Wissenschaft-1887-Nietzsche.djvu', 1, [50, 40], '영화 장면이 아니라, ‘신은 죽었다’는 말이 실린 니체의 『즐거운 학문』(1887년 판) 속표지예요 · 자료: 프리드리히 니체 · 퍼블릭 도메인 · 위키미디어 공용', '독일어 제목이 찍힌 옛 책의 속표지.'),
('ff-leftbehind', 'Hieronymus_Bosch_013.jpg', None, [50, 22], '영화 장면이 아니라, 하늘로 들려 올라가는 사람들을 그린 히에로니무스 보스의 「축복받은 이들의 승천」(1505~1515 무렵)이에요 · 그림: 히에로니무스 보스 · 퍼블릭 도메인 · 위키미디어 공용', '어두운 하늘을 지나 빛나는 둥근 통로 끝으로 천사들이 사람들을 데려가는 그림.'),
('ff-inchon', 'Landing_craft_approaching_Inchon,_Korea,_on_15_September_1950_(NH_42351).jpg', None, [50, 50], '영화 장면이 아니라, 1950년 9월 15일 인천 레드 비치로 다가가는 상륙정이에요 · 사진: 미국 해군 · 퍼블릭 도메인 · 위키미디어 공용', '물보라를 일으키며 해안으로 다가가는 작은 배들을 위에서 본 흑백 사진.'),
('ff-calling', 'Aerial_view_of_the_Amazon_Rainforest.jpg', None, [50, 50], '다큐 장면이 아니라, 하늘에서 본 브라질 아마존 밀림과 솔리몽이스강이에요 · 사진: lubasi · CC BY-SA 2.0 · 위키미디어 공용', '끝없는 초록 숲 사이로 넓은 강이 구불구불 흐르는 항공 사진.'),
('ff-okhanheum', 'Duccio_di_Buoninsegna,_The_Calling_of_the_Apostles_Peter_and_Andrew,_1308-1311,_NGA_282.jpg', None, [50, 50], '다큐 장면이 아니라, 어부들을 제자로 부르는 장면을 그린 두초의 그림(1308~1311)이에요 · 그림: 두초, 미국 국립미술관 · CC0 · 위키미디어 공용', '금빛 하늘 아래, 배 위의 두 어부를 물가의 예수가 부르는 그림.'),
('an-prince', '1904_Lawrence_Alma-Tadema_-_The_Finding_of_Moses.jpg', None, [50, 55], '애니메이션 장면이 아니라, 아기 모세를 찾은 이집트 공주의 행렬을 그린 로런스 앨마태디마의 그림(1904)이에요 · 그림: 로런스 앨마태디마 「모세의 발견」 · 퍼블릭 도메인 · 위키미디어 공용', '나일강 가, 가마에 탄 공주 앞으로 시종들이 아기 바구니를 들고 가는 화려한 그림.'),
('an-miracle', 'Ilja_Jefimowitsch_Repin_013.jpg', None, [58, 50], '애니메이션 장면이 아니라, 야이로의 딸을 살리는 장면을 그린 일리야 레핀의 그림(1871)이에요 · 그림: 일리야 레핀 · 퍼블릭 도메인 · 위키미디어 공용', '어두운 방, 침상에 누운 소녀 곁에 선 예수와 등불 빛에 비친 사람들.'),
('an-kingofkings', 'Dickens_dream.jpg', None, [50, 50], '애니메이션 장면이 아니라, 이야기꾼 찰스 디킨스를 그린 로버트 버스의 「디킨스의 꿈」(1875)이에요 · 그림: 로버트 윌리엄 버스 · 퍼블릭 도메인 · 위키미디어 공용', '의자에 앉아 조는 디킨스 둘레로 소설 인물들이 연필 스케치로 떠도는 미완성 그림.'),
('an-superbook', 'Lesendes_Mädchen_mit_Spitzenhaube_(1875)_-_Albert_Anker.jpg', None, [50, 45], '애니메이션 장면이 아니라, 책에 푹 빠진 아이를 그린 알베르트 앙커의 그림(1875)이에요 · 그림: 알베르트 앙커 「책 읽는 소녀」 · 퍼블릭 도메인 · 위키미디어 공용', '레이스 모자를 쓴 소녀가 책을 펼쳐 들고 읽는 그림.'),
('an-veggie', 'Tomate_rouge_grosse_hâtive_Vilmorin-Andrieux_1904.png|Concombre_blanc_très_gros_de_Bonneuil_Vilmorin-Andrieux_1883.png', None, [50, 50], '애니메이션 장면이 아니라, 옛 채소 그림책에 실린 토마토와 오이예요(1883·1904년) · 그림: 빌모랭앙드리외 · 퍼블릭 도메인 · 위키미디어 공용', '옛 채소 그림책의 흑백 판화 두 장. 위에는 열매 달린 토마토 포기와 큰 토마토, 아래에는 길쭉한 흰 오이.'),
('an-jw', 'Watchtower_Bible_&_Tract_Society_(world_headquarters).jpg', None, [50, 50], '애니메이션 장면이 아니라, 여호와의 증인의 옛 세계 본부(뉴욕 브루클린)예요. 지금 본부는 뉴욕주 워릭에 있어요 · 사진: Sergio Herrera · CC BY-SA 2.0 · 위키미디어 공용', '강가에 늘어선 붉은 벽돌 건물들.'),
('an-kells', 'KellsFol034rChiRhoMonogram.jpg', None, [50, 40], '애니메이션 장면이 아니라, 애니메이션의 바탕이 된 『켈스의 서』의 키로 쪽(34r, 800년 무렵)이에요 · 자료: 『켈스의 서』, 더블린 트리니티 칼리지 · 퍼블릭 도메인 · 위키미디어 공용', '그리스 글자 키와 로를 소용돌이 무늬로 가득 채워 크게 그린 필사본 쪽.'),
('an-hunchback', 'Charles_Meryon,_Le_stryge_(The_Vampire),_1853,_NGA_11635.jpg', None, [45, 40], '애니메이션 장면이 아니라, 노트르담 대성당 위 괴물 조각을 새긴 샤를 메리옹의 판화 「흡혈귀」(1853)예요 · 그림: 샤를 메리옹, 미국 국립미술관 · CC0 · 위키미디어 공용', '대성당 난간에 턱을 괴고 앉은 날개 달린 괴물 조각 너머로 파리 시내가 내려다보이는 판화.'),
('an-heidi', 'Heidiland_(Maienfeld_(Graubünden_(Schweiz))).jpg', None, [50, 50], '애니메이션 장면이 아니라, 제작진이 직접 찾아갔던 스위스 마이엔펠트의 풍경이에요 · 사진: Marc Gabriel Schmid · CC BY-SA 4.0 · 위키미디어 공용', '푸른 풀밭 너머로 높은 알프스 산이 보이는 마을 풍경.'),
('gm-carcassonne', '1_carcassonne_aerial_2016.jpg', None, [50, 50], '게임 그림이 아니라, 게임 이름이 된 프랑스의 성벽 도시 카르카손이에요 · 사진: Chensiyuan · CC BY-SA 4.0 · 위키미디어 공용', '두 겹 성벽과 뾰족한 탑들로 둘러싸인 언덕 위 중세 도시를 하늘에서 본 모습.'),
('gm-pillars', 'Joseph_Mallord_William_Turner_-_South_view_of_Salisbury_Cathedral_from_the_Cloisters,_1802_-_Victoria_and_Albert_Museum,_London.jpg', None, [50, 45], '게임 그림이 아니라, 소설 속 킹스브리지 대성당의 바탕이 된 솔즈베리 대성당을 그린 윌리엄 터너의 그림(1802)이에요 · 그림: J. M. W. 터너, 빅토리아 앨버트 미술관 · 퍼블릭 도메인 · 위키미디어 공용', '회랑 너머로 높이 솟은 고딕 대성당의 남쪽 모습을 그린 수채화.'),
('gm-notredame', "Notre-Dame,_le_chevet_et_le_pont_de_l'Archevêché._G.4836(3).jpg", None, [55, 50], '게임 그림이 아니라, 노트르담 대성당과 그 곁 동네를 새긴 샤를 메리옹의 판화(19세기)예요 · 그림: 샤를 메리옹, 파리 박물관(Paris Musées) · CC0 · 위키미디어 공용', '센강 다리 너머로 노트르담 대성당의 뒤쪽이 보이는 흑백 판화.'),
('gm-dutchblitz', 'Mascot_Mills_Barn_w_Hexes_LanCo_PA.JPG', None, [50, 50], '게임 그림이 아니라, 게임이 태어난 펜실베이니아 더치 지역의 헛간이에요. 둥근 ‘헥스 사인’으로 꾸몄어요 · 사진: Smallbones · CC BY-SA 3.0 · 위키미디어 공용', '붉은 헛간 벽에 둥근 별 무늬 장식이 여러 개 걸린 모습.'),
('gm-pentiment', 'Nuremberg_chronicles_-_PATAVIA.png', None, [50, 50], '게임 그림이 아니라, 제작진이 연구한 『뉘른베르크 연대기』(1493)의 목판화예요. 바이에른의 도시 파사우를 새겼어요 · 그림: 미하엘 볼게무트·빌헬름 플라이덴부르프 · 퍼블릭 도메인 · 위키미디어 공용', '강가에 성벽과 교회 탑이 빽빽한 옛 도시를 새긴 목판화.'),
('gm-kingdomcome', '100822_Sazava_Klaster_0019.JPG', None, [50, 50], '게임 그림이 아니라, 1편의 무대인 체코 사자바 수도원이에요 · 사진: svajcr · CC BY-SA 3.0 · 위키미디어 공용', '탑이 있는 옛 수도원 건물.'),
('gm-blasphemous', 'Francisco_de_Goya_-_Los_disciplinantes_-_Google_Art_Project.jpg', None, [50, 55], '게임 그림이 아니라, 게임에 녹아 있다는 고야의 「채찍질 고행자들의 행렬」(1812~1819)이에요 · 그림: 프란시스코 고야, 산 페르난도 왕립 미술 아카데미 · 퍼블릭 도메인 · 위키미디어 공용', '뾰족한 흰 두건을 쓴 고행자들과 성상 가마를 둘러싼 군중의 행렬 그림.'),
('gm-dante', 'Gustave_Doré_-_Dante_Alighieri_-_Inferno_-_Plate_9_(Canto_III_-_Charon).jpg', None, [50, 40], '게임 그림이 아니라, 『신곡』 지옥 편의 뱃사공 카론을 그린 귀스타브 도레의 판화(1861)예요 · 그림: 귀스타브 도레 · 퍼블릭 도메인 · 위키미디어 공용', '어두운 강 위로 노를 든 뱃사공이 다가오고 강가에 영혼들이 모여 있는 흑백 판화.'),
('gm-isaac', 'Sacrifice_of_Isaac-Caravaggio_(Uffizi).jpg', None, [50, 45], '게임 그림이 아니라, 제목의 바탕이 된 창세기 ‘이삭을 바침’ 장면을 그린 카라바조의 그림(1603 무렵)이에요 · 그림: 카라바조, 우피치 미술관 · 퍼블릭 도메인 · 위키미디어 공용', '천사가 칼을 든 아브라함의 손을 붙잡아 멈추게 하는 장면을 그린 그림.'),
# 1장 기다림과 성탄
('mk-nutcracker', 'Nussknackermuseum_002.jpg', None, [50, 50], '사진: René Röder · CC BY-SA 3.0 · 위키미디어 공용(독일 노이하우젠 호두까기 인형 박물관)', '선반 가득 늘어선 색색의 나무 호두까기 인형들.'),
('read-martin', 'Makowski_Shoemaker.jpg', None, [50, 50], '책 그림이 아니라, 구두를 고치는 사람을 그린 타데우시 마코프스키의 그림(1930)이에요 · 그림: 타데우시 마코프스키 「구두장이」 · 퍼블릭 도메인 · 위키미디어 공용', '작은 방에서 구두를 고치는 사람을 단순한 선과 따뜻한 색으로 그린 그림.'),
('oc-jan7', 'Nativity_(15th_c.,_Annunciation_Cathedral_in_Moscow).jpg', None, [50, 45], '그림: 안드레이 루블료프(로 전함) 「성탄」 이콘, 모스크바 크렘린 성모 영보 대성당 · 퍼블릭 도메인 · 위키미디어 공용', '동굴 안 구유에 누운 아기와 마리아, 둘레의 천사와 목자들을 금빛 바탕에 그린 이콘.'),
('oc-alilo', 'Alilo_2008.jpg', None, [50, 50], '사진: Paata Vardanashvili · CC BY 2.0 · 위키미디어 공용(2008년 1월, 조지아 트빌리시)', '흰 옷 차림의 사람들과 깃발이 거리를 가득 메운 성탄 행렬.'),
('oc-nameday', 'Constantine_and_Helen.png', None, [50, 40], '5월 21일에 함께 기억하는 콘스탄티누스와 헬레나의 이콘이에요 · 그림: 엠마누엘 차네스(1669) · 퍼블릭 도메인 · 위키미디어 공용', '십자가를 가운데 두고 왕관을 쓴 콘스탄티누스와 헬레나가 나란히 선 이콘.'),
('craft-bombki', 'Bombki_choinkowe-2023.12.31.jpg', None, [50, 50], '사진: Aw58 · CC BY-SA 4.0 · 위키미디어 공용', '전나무 가지에 매달린, 손으로 무늬를 그린 유리 장식 공들.'),
# 2장 고난과 부활
('hw-oberammergau', 'The_Kreusigungsgruppe,_Oberammergau,_Upper_Bavaria,_Germany-LCCN2002696268.jpg', None, [50, 50], '공연 사진이 아니라, 1871년 수난극을 보고 감동한 바이에른 왕 루트비히 2세가 마을에 선물한 십자가상이에요(1890~1900년 무렵 색을 입혀 찍은 포토크롬) · 자료: 미국 의회도서관 포토크롬 모음 · 퍼블릭 도메인 · 위키미디어 공용', '푸른 하늘 아래 높은 돌 받침 위에 십자가에 달린 예수와 그 아래 양쪽에 선 두 인물상을 담은 옛 채색 사진.'),
# 3장 그림과 유리
('aa-watanabe', 'MET_DP13870.jpg', None, [50, 50], '작품이 아니라, 와타나베가 쓴 일본 염색 기법 ‘가타조메’의 종이 본(19세기)이에요 · 자료: 일본 가타가미, 메트로폴리탄 미술관 · CC0 · 위키미디어 공용', '갈색 종이에 새와 물결 무늬를 오려 낸 염색용 종이 본.'),
('aa-leenamgyu', 'Myeongdong_Cathedral_6.jpg', None, [50, 45], '작품 사진이 아니라, 그의 유리화(1980~1984년)가 있는 서울 명동대성당이에요 · 사진: kallerna · CC BY-SA 4.0 · 위키미디어 공용', '붉은 벽돌에 높은 첨탑이 솟은 명동대성당과 주변 건물.'),
('bq-elgreco', 'Pentecostés_(El_Greco,_c._1600)_Prado.jpg', None, [50, 40], '그림: 엘 그레코 「성령강림」(1596~1600 무렵), 프라도 미술관 · 퍼블릭 도메인 · 위키미디어 공용', '마리아와 사도들 머리 위로 불꽃이 내려앉고 위에서 비둘기가 빛을 내는, 세로로 긴 그림.'),
# 4장 책이 된 말씀
('keep-tischendorf', 'Codex_Sinaiticus_Matthew_6,4-32.JPG', None, [50, 50], '인물 사진이 아니라, 티셴도르프가 세상에 알린 시나이 사본의 한 쪽(마태복음, 4세기)이에요 · 자료: 시나이 사본, 영국 도서관 · 퍼블릭 도메인 · 위키미디어 공용', '누렇게 바랜 양피지에 그리스어 대문자가 여러 단으로 빼곡히 적힌 쪽.'),
('wd-phrases', 'Rembrandt-Belsazar.jpg', None, [40, 45], '그림: 렘브란트 「벨사살의 잔치」, 런던 내셔널 갤러리 · 퍼블릭 도메인 · 위키미디어 공용', '잔치 자리에서 왕이 벽에 나타난 빛나는 글씨를 보고 놀라 몸을 돌리는 그림.'),
('nb-chagall', 'Aerial_view_of_Jerusalem_from_the_southwest_LOC_matpc.13643.jpg', None, [50, 50], '판화가 아니라, 샤갈이 1931년에 다녀온 예루살렘의 1930년대 항공 사진이에요 · 사진: 매트슨 사진 모음, 미국 의회도서관 · 퍼블릭 도메인 · 위키미디어 공용', '성벽에 둘러싸인 예루살렘 옛 도시와 둘레 동네를 하늘에서 본 흑백 사진.'),
('nb-stjohns', '2009-0522-MN-SJU-abbeychurch.jpg', None, [50, 50], '성경 그림이 아니라, 이 성경을 만든 미국 미네소타의 세인트 존스 수도원 성당이에요 · 사진: Bobak Ha’Eri · CC BY 3.0 · 위키미디어 공용', '벌집 무늬 벽 앞에 커다란 콘크리트 종탑이 선 현대식 성당.'),
('bb-barton', 'CodxAmiatinusFolio5rEzra.jpg', None, [50, 45], '책 사진이 아니라, 책을 베껴 쓰는 학자 에스라를 그린 아미아티누스 사본(700년 무렵)의 쪽이에요 · 자료: 아미아티누스 사본, 피렌체 라우렌치아나 도서관 · 퍼블릭 도메인 · 위키미디어 공용', '책장이 있는 방에서 학자가 무릎 위 책에 글을 쓰는 필사본 그림.'),
('bb-stone', "Bifolio_from_Paul's_Letter_to_the_Romans,_the_end_of_Paul's_Letter_to_the_Philippians_and_the_beginning_of_Paul's_Letter_to_the_Colossians.jpg", None, [30, 50], '책 사진이 아니라, 바울 서신이 적힌 아주 오래된 파피루스(P46, 200년 무렵)예요 · 자료: 파피루스 P46 · 퍼블릭 도메인 · 위키미디어 공용', '갈색 파피루스 두 장에 그리스어 글씨가 빼곡히 남은 모습.'),
('bb-ehrman', 'Codex_Vaticanus_B,_2Thess._3,11-18,_Hebr._1,1-2,2.jpg', None, [50, 50], '책 사진이 아니라, 바티칸 사본(4세기)의 히브리서 첫 쪽이에요. 이 쪽 여백에는 글자를 고친 사람을 꾸짖는 옛 필사자의 메모가 남아 있어요 · 자료: 바티칸 사본 · 퍼블릭 도메인 · 위키미디어 공용', '누렇게 바랜 양피지에 그리스어 대문자가 세 단으로 적힌 쪽.'),
('bb-300', 'Harvard_drs_431802859_聖經直解_v.1.pdf', 11, [50, 50], '책 사진이 아니라, 조선 천주교 신자들이 읽던 한문 『성경직해』(베이징 판)의 쪽이에요 · 자료: 마누엘 디아스, 하버드 대학 도서관 · 퍼블릭 도메인 · 위키미디어 공용', '세로로 쓴 한문이 빼곡한 옛 책의 쪽.'),
('keep-najeeb', 'Our_Lady_of_the_Hour_Church.jpg', None, [50, 45], '인물 사진이 아니라, 모술의 도미니코회 ‘시계 성당’이에요(2024년 사진) · 사진: الدبوني · CC BY-SA 4.0 · 위키미디어 공용', '높은 시계탑이 있는 밝은 돌 성당.'),
# 5장 성당과 수도원, 순례길
('sai-lisieux', 'Basilique_Sainte-Thérèse_de_Lisieux-2876.jpg', None, [50, 50], '인물 사진이 아니라, 리지외의 성녀 데레사 대성당이에요 · 사진: Raimond Spekking · CC BY-SA 4.0 · 위키미디어 공용', '넓은 계단 위에 큰 돔과 탑을 얹은 흰 대성당.'),
('mar-bernadette', 'Lourdes_-_«_cachot_»_-_2.jpg', None, [50, 50], '인물 사진이 아니라, 베르나데트 가족이 살던 루르드의 옛 감옥 방 ‘카쇼’예요 · 사진: Peter Potrowl · CC BY-SA 4.0 · 위키미디어 공용', '흰 벽에 십자가가 걸리고 작은 벽난로가 있는 좁은 방.'),
('mon-nonnberg', '2163_-_Salzburg_-_Stift_Nonnberg.JPG', None, [50, 50], '인물 사진이 아니라, 잘츠부르크 언덕 위의 논베르크 수녀원이에요 · 사진: Andrew Bossi · CC BY-SA 2.5 · 위키미디어 공용', '숲 언덕 위에 수녀원과 교회 탑이 선 잘츠부르크 풍경.'),
# 6장 동방의 교회
('song-byzantine', 'Gb-LblHarley5544_fol13r.jpg', None, [50, 50], '자료: 비잔틴 성가 악보 필사본(17세기), 영국 도서관 할리 5544 · 퍼블릭 도메인 · 위키미디어 공용', '그리스어 가사 위에 붉고 검은 성가 기호가 줄지어 적힌 필사본.'),
('song-rachmaninoff', 'Levitan_Evening_bells_1892.jpg', None, [55, 45], '인물 사진이 아니라, 저녁 예배를 알리는 수도원 종소리를 그린 이사크 레비탄의 「저녁 종」(1892)이에요 · 그림: 이사크 레비탄 · 퍼블릭 도메인 · 위키미디어 공용', '저녁 햇살 속 강 건너 숲가에 하얀 수도원이 서 있는 그림.'),
('song-shchedryk', 'Hirundo_rustica._Naumann.jpg', None, [50, 50], '노래 속에서 풍성한 새해를 알려 주는 제비예요 · 그림: 나우만의 새 도감 · CC BY-SA 4.0 · 위키미디어 공용', '가지에 앉은 제비들을 그린 옛 새 그림.'),
('ib-athos', 'Simonopetra_Monastery,_Mount_Athos.jpg', None, [50, 50], '아토스산의 시모노스 페트라 수도원이에요 · 사진: Angelos @ Ottawa · 퍼블릭 도메인 · 위키미디어 공용', '바다 위 절벽 꼭대기에 층층이 세운 수도원.'),
('ib-printed', 'Святогорская_икона_Божией_Матери_(1569)._Чтец-8.jpg', None, [50, 45], '1885년 잡지에 색인쇄로 실린 「스뱌토고르스카야 성모」 이콘이에요 · 자료: 러시아 잡지 『독자』 · 퍼블릭 도메인 · 위키미디어 공용', '아기 예수를 안은 성모를 색인쇄로 찍은 종이 이콘.'),
('ib-ukraine', 'Марія_Єгипетська_з_житієм._Українська_ікона_кінця_XVII_ст._Село_Лісковате._-_Mary_of_Egypt_with_her_Life._Ukrainian_icon,_late_17th_century._Liskovate_village..jpg', None, [50, 45], '17세기 말 우크라이나 이콘 「이집트의 마리아와 생애」(리스코바테 마을)예요 · 사진: Hrom.nv · CC BY-SA 4.0 · 위키미디어 공용', '가운데 성녀를 크게 그리고 둘레 작은 칸에 그 생애 장면을 그린 이콘.'),
('ib-import', 'Icon_Our_Lady_of_Kazan._back_side._Mid_19th-century.jpg', None, [50, 50], '19세기 중반 「카잔의 성모」 이콘의 뒷면이에요 · 사진: Dmitry Makeev · CC BY-SA 4.0 · 위키미디어 공용', '나무판을 가로대로 이은 이콘의 뒷면.'),
('song-zvon', 'Звонница_Ростов_3.jpg', None, [50, 50], '로스토프 크렘린 종탑의 종이에요 · 사진: Ulaisaeva · CC BY-SA 4.0 · 위키미디어 공용', '종탑에 매달린 커다란 청동 종.'),
# 8장 노래가 된 믿음
('hymn-well', 'Episodes_du_naufrage_du_steamer_la_Ville-du-Havre_(Monde_illustré,_1873-12-13).jpeg', None, [50, 50], '인물 사진이 아니라, 스패포드의 네 딸이 숨진 빌 뒤 아브르호 침몰을 그린 1873년 신문 판화예요 · 그림: 다니엘 비에르주 · 퍼블릭 도메인 · 위키미디어 공용', '가라앉는 배와 구명보트를 여러 칸으로 그린 옛 신문 판화.'),
('hymn-crosby', 'New_York_Institution_for_the_Blind_(NYPL_b13476048-422070).jpg', None, [50, 50], '인물 사진이 아니라, 크로스비가 공부하고 가르친 뉴욕 맹아학교를 그린 19세기 판화예요 · 자료: 뉴욕 공공도서관 · 퍼블릭 도메인 · 위키미디어 공용', '뾰족한 탑이 있는 큰 석조 학교 건물을 그린 옛 판화.'),
('hymn-jesusloves', "Bradbury's_golden_shower_of_S.S._melodies_-_a_new_collection_of_hymns_and_tunes_for_the_Sabbath_school_(IA_bradburysgoldens00brad).pdf", 1, [50, 50], '인물 사진이 아니라, 이 노래가 실린 브래드버리의 주일학교 노래책 『골든 샤워』(1862)의 표지예요 · 자료: 윌리엄 B. 브래드버리 · 퍼블릭 도메인 · 위키미디어 공용', '옛 노래책의 장식 표지.'),
('spir-fisk', 'Jubilee_Hall,_Fisk_University.jpg', None, [50, 50], '인물 사진이 아니라, 노래로 모은 돈으로 지은 피스크 대학교 주빌리 홀이에요(1910년 무렵) · 사진: 작자 미상 · 퍼블릭 도메인 · 위키미디어 공용', '높은 탑이 있는 대학 건물의 옛 사진.'),
('spir-mahalia', 'Mahalia_Jackson_Theater_for_the_Performing_Arts.jpg', None, [50, 50], '인물 사진이 아니라, 그의 이름을 딴 뉴올리언스의 마할리아 잭슨 극장이에요 · 사진: Robbie Mendelson · CC BY-SA 2.0 · 위키미디어 공용', '분수 너머로 보이는 현대식 극장 건물.'),
('ns-part', 'Lääne-Harju_vald_(51003853625).jpg', None, [50, 50], '인물 사진이 아니라, 에스토니아 라울라스마의 아르보 패르트 센터예요 · 사진: Sergei Gussev · CC BY 2.0 · 위키미디어 공용', '나무 판으로 마감한 둥근 벽이 이어지는 조용한 실내.'),
('ns-jcs', 'Giotto_-_Scrovegni_-_-31-_-_Kiss_of_Judas.jpg', None, [50, 45], '공연 사진이 아니라, 뮤지컬의 한가운데 있는 유다의 입맞춤을 그린 조토의 벽화(1305 무렵)예요 · 그림: 조토, 파도바 스크로베니 경당 · 퍼블릭 도메인 · 위키미디어 공용', '횃불과 창을 든 군중 한가운데서 유다가 예수에게 입을 맞추는 벽화.'),
('spir-swinglow', 'Giuseppe_Angeli,_Elijah_Taken_Up_in_a_Chariot_of_Fire,_c._1740-1755,_NGA_41685.jpg', None, [50, 45], '노래 속 ‘마차’의 바탕인, 엘리야를 하늘로 데려간 불 수레를 그린 주세페 안젤리의 그림(1740~1755 무렵)이에요 · 그림: 미국 국립미술관 · CC0 · 위키미디어 공용', '구름 사이로 말이 끄는 불 수레에 탄 노인이 하늘로 올라가는 그림.'),
('hymn-precious', 'Pilgrim_Baptist_HABS_ILL-1054.jpg', None, [50, 50], '인물 사진이 아니라, 도시가 음악 감독으로 일한 시카고 필그림 침례교회예요(1964년 사진) · 사진: 해럴드 앨런 · 퍼블릭 도메인 · 위키미디어 공용', '아치 창이 줄지은 석조 교회 건물의 흑백 사진.'),
('ns-joseph', 'La_túnica_de_José,_by_Diego_Velázquez.jpg', None, [50, 50], '공연 사진이 아니라, 피 묻은 요셉의 옷을 아버지 야곱에게 보이는 장면을 그린 벨라스케스의 그림(1630)이에요 · 그림: 디에고 벨라스케스, 엘 에스코리알 · 퍼블릭 도메인 · 위키미디어 공용', '형제들이 옷을 펼쳐 보이자 늙은 아버지가 두 팔을 들고 놀라는 그림.'),
('ns-lesmis', 'Ebcosette.jpg', None, [50, 45], '공연 사진이 아니라, 뮤지컬 포스터의 바탕이 된 에밀 바야르의 코제트 삽화(1862)예요 · 그림: 에밀 바야르 · 퍼블릭 도메인 · 위키미디어 공용', '커다란 빗자루를 든 작은 소녀가 맨발로 서 있는 흑백 삽화.'),
# 9장 책 속 이야기
('lit-idiot', 'The_Body_of_the_Dead_Christ_in_the_Tomb_(detail,_head)_by_Hans_Holbein_d._j.jpg', None, [55, 50], '작가 사진이 아니라, 소설 속 인물들이 이야기하는 한스 홀바인의 「무덤 속 그리스도의 시신」(1521~1522)의 부분이에요 · 그림: 한스 홀바인, 바젤 미술관 · 퍼블릭 도메인 · 위키미디어 공용', '좁은 관 속에 누운 야윈 그리스도의 얼굴과 어깨를 그린 그림의 부분.'),
('el-yundongju', '윤동주_문학관_180707_02.jpg', None, [50, 50], '인물 사진이 아니라, 서울 종로구 청운동의 윤동주 문학관이에요 · 사진: Jjw · CC BY-SA 4.0 · 위키미디어 공용', '하늘이 뚫린 콘크리트 벽 사이의 좁은 마당.'),
('el-faithpoems', '정지용_생가_(3).JPG', None, [70, 60], '인물 사진이 아니라, 충북 옥천의 정지용 생가예요 · 사진: Jocelyndurrey · CC BY-SA 4.0 · 위키미디어 공용', '마당 앞에 선 초가지붕을 얹은 낮은 흙벽 집.'),
('el-martyred', 'Prayer_meeting,_Pyeng_Yang,_(s.d.)_(Taylor_box21num64).jpg', None, [50, 50], '작가 사진이 아니라, 소설의 무대인 평양의 옛 기도 모임 사진이에요(1908~1922년 사이) · 사진: 미국 감리교회 선교부 · 퍼블릭 도메인 · 위키미디어 공용', '넓은 방을 가득 메운 사람들이 앉아 있는 옛 흑백 사진.'),
('pb-prince', 'Plate_1_of_The_Happy_Prince_and_Other_Tales_(1888).png', None, [50, 40], '그림: 월터 크레인, 『행복한 왕자와 다른 이야기』 첫판(1888) 삽화 · 퍼블릭 도메인 · 위키미디어 공용', '높은 기둥 위의 왕자 동상과 그 곁을 나는 제비를 그린 흑백 삽화.'),
('pb-giant', '"The_Selfish_Giant"_from_the_"The_Happy_Prince"_-_The_art_of_Walter_Grane_(page_180_crop).jpg', None, [50, 45], '그림: 월터 크레인, 『행복한 왕자와 다른 이야기』 첫판(1888)의 「거인의 정원」 삽화 · 퍼블릭 도메인 · 위키미디어 공용', '꽃 핀 나무 아래 거인과 작은 아이를 그린 흑백 삽화.'),
('pb-clown', 'Juggler_from_Harley_ms_4951_folio_298v.jpg', None, [50, 40], '책 그림이 아니라, 11세기 필사본에 그려진 저글러예요. 이 그림책은 ‘성모의 곡예사’라는 중세 전설에서 왔어요 · 자료: 영국 도서관 할리 4951 · 퍼블릭 도메인 · 위키미디어 공용', '작은 공 여러 개를 공중에 던지며 재주를 부리는 사람을 그린 옛 필사본 그림.'),
('pb-noah', "Noah's_Ark_by_Edward_Hicks,_1846_(Philadelphia_museum_of_art).jpg", None, [50, 50], '책 그림이 아니라, 같은 이야기를 그린 에드워드 힉스의 「노아의 방주」(1846)예요 · 그림: 에드워드 힉스, 필라델피아 미술관 · CC0 · 위키미디어 공용', '짐승들이 둘씩 짝지어 큰 나무 방주로 줄지어 들어가는 그림.'),
('pb-pienkowski', 'Krippenengel_Silhouette.jpg', None, [50, 40], '책 그림이 아니라, 성탄 구유 장식의 천사 실루엣이에요 · 사진: Anna reg · CC BY-SA 3.0 · 위키미디어 공용', '창밖 빛을 등지고 선, 날개를 편 검은 천사 실루엣.'),
('pb-storybible', 'Christ_Blessing_the_Children_MET_DP280362.jpg', None, [50, 45], '책 그림이 아니라, 아이들을 안고 축복하는 예수를 그린 루카스 크라나흐(아들)의 그림(1545 무렵)이에요 · 그림: 메트로폴리탄 미술관 · CC0 · 위키미디어 공용', '엄마들이 안고 온 아이들을 예수가 품에 안고 축복하는 그림.'),
('mg-saintyoung', 'Buildings_in_Tachikawa.jpg', None, [50, 50], '만화 그림이 아니라, 두 주인공이 사는 도쿄 다치카와의 거리예요 · 사진: Syced · CC0 · 위키미디어 공용', '둥근 지붕 건물과 빌딩들이 보이는 도쿄 교외 도시 풍경.'),
('mg-mangabible', 'Gustave_Doré_-_The_Holy_Bible_-_Plate_I,_The_Deluge.jpg', None, [50, 45], '만화 그림이 아니라, 성경 이야기를 극적인 그림으로 옮긴 귀스타브 도레의 「대홍수」(1866)예요 · 그림: 귀스타브 도레 · 퍼블릭 도메인 · 위키미디어 공용', '거센 물결 속 바위에 매달린 사람들을 그린 흑백 판화.'),
('mg-crumb', 'Pieter_Bruegel_the_Elder_-_The_Tower_of_Babel_(Vienna)_-_Google_Art_Project_-_edited.jpg', None, [45, 50], '만화 그림이 아니라, 창세기 11장의 바벨탑을 그린 피터르 브뤼헐의 그림(1563)이에요 · 그림: 피터르 브뤼헐, 빈 미술사 박물관 · 퍼블릭 도메인 · 위키미디어 공용', '바닷가 도시 위로 층층이 솟은 거대한 둥근 탑을 짓는 사람들을 그린 그림.'),
# 11장 곁을 지킨 사람들
('res-kolbe', 'Niepokalanow_basilica_fc05.jpg', None, [50, 50], '인물 사진이 아니라, 콜베 신부가 세운 폴란드 니에포칼라누프 수도원의 대성당이에요 · 사진: Fczarnowski · CC BY-SA 3.0 · 위키미디어 공용', '넓은 마당 뒤로 높은 흰 대성당이 선 모습.'),
('res-sendler', 'Fragments_ghetto_walls_Warsaw.jpg', None, [50, 50], '인물 사진이 아니라, 바르샤바 시에나 거리에 남은 게토 담장의 한 조각이에요 · 사진: Saifunny · CC BY-SA 4.0 · 위키미디어 공용', '건물 마당 안쪽에 남은 붉은 벽돌 담과 안내판.'),
('res-jager', 'Kirche_StRadegund.JPG', None, [50, 50], '인물 사진이 아니라, 예거슈테터가 성당지기로 일한 오스트리아 장크트 라데군트 성당이에요 · 사진: Sziklai · CC BY-SA 3.0 · 위키미디어 공용', '안개 낀 날, 뾰족한 탑이 있는 작은 시골 성당.'),
('care-damien', 'St._Philomena_Catholic_Church,_Kalawao,_1905.jpg', None, [50, 50], '인물 사진이 아니라, 다미안 신부가 몰로카이섬 칼라와오에서 넓혀 지은 성 필로메나 성당이에요(1905년 사진) · 사진: 작자 미상 · 퍼블릭 도메인 · 위키미디어 공용', '바다와 절벽을 등지고 선 작은 흰 목조 성당의 흑백 사진.'),
('care-marianne', 'Kalaupapa_Peninsula_92.jpg', None, [50, 50], '인물 사진이 아니라, 마리안 수녀가 한센병 환자들과 살았던 몰로카이섬 칼라우파파 반도예요 · 사진: Gillfoto · CC BY-SA 4.0 · 위키미디어 공용', '높은 절벽 아래 바다로 뻗은 평평한 초록 반도.'),
('ms-liddell', 'Carte_postale_-_Colombes_-_Stade_Olympique_de_Colombes.jpg', None, [50, 50], '인물 사진이 아니라, 리들이 400미터에서 금메달을 딴 1924년 파리 올림픽의 콜롱브 경기장이에요(옛 엽서) · 자료: 작자 미상 · 공개 라이선스(Licence Ouverte) · 위키미디어 공용', '관중석에 둘러싸인 큰 경기장의 옛 흑백 엽서.'),
# 12장 이 땅의 이야기
('kor-leetaeseok', 'Tonj_Catholic_Church.JPG', None, [45, 50], '인물 사진이 아니라, 이태석 신부가 일한 남수단 톤즈의 돈 보스코 선교회 성당이에요 · 사진: Ernst Ulz · CC BY-SA 3.0 · 위키미디어 공용', '붉은 흙 마당 위에 선 소박한 벽돌 성당.'),
('kb2-1911', '1911_Old_Testament_translated_in_Korean_language.jpg', None, [50, 50], '자료: 1911년 한국어로 옮긴 구약 성경 · 퍼블릭 도메인 · 위키미디어 공용', '세로로 쓴 옛 한글이 빼곡한, 펼쳐 놓은 낡은 성경책.'),
('kb2-1938', '셩경_개역.pdf', 1, [50, 45], '자료: 『셩경 개역』(1938) 속표지 · 퍼블릭 도메인 · 위키미디어 공용', '‘셩경 개역’이라는 큰 글자가 세로로 찍힌 속표지.'),
('kb2-common', 'Angelos_Akotantos_(active_1436-1450)_-_Icon_of_The_Embrace_of_the_Apostles_Peter_and_Paul_-_WA1982.192_-_Ashmolean_Museum.jpg', None, [50, 40], '책 사진이 아니라, 하나 됨을 그린 옛 이콘 「베드로와 바울의 포옹」(15세기)이에요 · 그림: 안겔로스 아코탄토스, 옥스퍼드 애시몰린 박물관 · 퍼블릭 도메인 · 위키미디어 공용', '금빛 바탕에 두 사도가 서로 끌어안은 모습을 그린 이콘.'),
('kb2-1998', 'Camel_MET_DT4913.jpg', None, [50, 50], '‘약대’라고 옮기던 동물, 낙타예요 · 그림: 12세기 스페인 성당 벽화, 메트로폴리탄 미술관 · CC0 · 위키미디어 공용', '흰 벽에 갈색으로 그린 혹 달린 낙타.'),
('kb2-catholic', 'Albrecht_Dürer,_Saint_Jerome_in_His_Study,_1514,_NGA_6642.jpg', None, [50, 50], '책 사진이 아니라, 성경 번역의 상징인 성 예로니모를 새긴 알브레히트 뒤러의 판화(1514)예요 · 그림: 미국 국립미술관 · CC0 · 위키미디어 공용', '햇빛 드는 서재에서 노학자가 책상에 앉아 글을 쓰고, 앞에 사자가 엎드린 판화.'),
('kb2-saehangeul', 'Hunminjeongeum_Haerye_03.jpg', None, [50, 50], '책 사진이 아니라, 한글을 처음 세상에 알린 『훈민정음 해례본』(1446)의 쪽이에요 · 자료: 조선 정부 · 퍼블릭 도메인 · 위키미디어 공용', '한문과 한글 자모가 세로로 찍힌 옛 책의 두 쪽.'),
('kl-seoseopyeong', '광주광역시_양림역사문화마을_입구.jpg', None, [50, 55], '인물 사진이 아니라, 서서평이 일한 광주 양림동 역사문화마을이에요 · 사진: NZ 토끼들 · CC BY-SA 4.0 · 위키미디어 공용', '양림역사문화마을 입구 길.'),
('kl-seal', 'Denmark,_First_Christmas_Seal,_1904.jpg', None, [50, 50], '한국 첫 실이 아니라, 1904년 덴마크에서 처음 나온 크리스마스 실이에요 · 자료: 덴마크 크리스마스 실 재단 · 퍼블릭 도메인 · 위키미디어 공용', '‘JULEN 1904’ 글자와 왕비의 얼굴을 보라색으로 찍은 작은 실.'),
('kch-dudong', 'Iksan_City_21_(16610664033).jpg', None, [50, 55], '익산 두동교회 옛 예배당이에요 · 사진: 대한민국 정부(코리아넷) · CC BY-SA 2.0 · 위키미디어 공용', '기와를 얹은 한옥식 작은 예배당.'),
('kch-cheongna', '선교사_스윗즈_주택.jpg', None, [50, 55], '청라언덕의 선교사 스윗즈 주택이에요 · 사진: 최옥석 · CC BY-SA 4.0 · 위키미디어 공용', '붉은 벽돌과 기와지붕이 어우러진 옛 선교사 주택.'),
('kch-underwood', 'Horace_Grant_Underwood_statue_in_Yonsei_Univ_main_campus.jpg', None, [50, 35], '기념관 사진이 아니라, 같은 연세대 신촌 캠퍼스에 있는 호러스 언더우드 동상이에요 · 사진: Rickinasia · CC BY-SA 4.0 · 위키미디어 공용', '높은 받침대 위에 선 선교사 동상.'),
('km-soongsil', 'Soongsil_University_2.JPG', None, [50, 50], '박물관 사진이 아니라, 박물관이 있는 숭실대학교의 정문이에요 · 사진: hyolee2 · CC BY-SA 3.0 · 위키미디어 공용', '대학 정문과 건물들.'),
('km-history', 'Typewriter_Underwood_1945.jpg', None, [50, 55], '전시관 사진이 아니라, 전시품 가운데 하나와 같은 회사의 언더우드 타자기(1945년 모델)예요 · 사진: Ivan2010 · CC BY-SA 3.0 · 위키미디어 공용', '둥근 자판이 줄지은 검은 옛 타자기.'),
('ksg-saebyeok', 'Sorae_korea_church_1895.jpeg', None, [50, 50], '새벽송 이야기가 전하는 황해도 소래교회예요(1895년 무렵) · 사진: 릴리어스 H. 언더우드(1908년 책) · 퍼블릭 도메인 · 위키미디어 공용', '기와를 얹은 작은 한옥 예배당의 옛 흑백 사진.'),
('ksg-maria', 'La_Tour_-_La_Madeleine_à_la_veilleuse_dite_La_Madeleine_Terff,_vers_1642_-_1644,_RF_1949_11.jpg', None, [45, 50], '공연 사진이 아니라, 막달라 마리아를 그린 조르주 드 라 투르의 「등불 앞의 막달라 마리아」(1642~1644 무렵)예요 · 그림: 루브르 박물관 · 퍼블릭 도메인 · 위키미디어 공용', '어두운 방, 등잔불 앞에 앉은 여인이 생각에 잠긴 그림.'),
# 공공누리·추가로 찾은 카드 (2026-11-17 밤)
('km-bskorea', '신약젼셔_(1904년).pdf', 1, [50, 45], '전시실 사진이 아니라, 1904년에 나온 한글 신약 『신약젼셔』의 첫 쪽이에요 · 자료: 성경번역자회(Bible Committee of Korea) · 퍼블릭 도메인 · 위키미디어 공용', '누렇게 바랜 종이에 ‘신약젼셔’라는 큰 글자가 세로로 찍힌 옛 책의 첫 쪽.'),
('ksg-first', '찬송가(UNION_HYMNAL).jpg', None, [24, 50], '첫 찬송가집 사진이 아니라, 장로교와 감리교가 처음 함께 펴낸 1908년 『찬송가』예요. 이 책도 악보 없이 가사만 실었어요(국가등록문화유산) · 사진: 문화재청(지금 국가유산청) · 공공누리 제1유형 · 위키미디어 공용', '닳은 붉은 표지의 손바닥만 한 옛 찬송가 책.'),
('ksg-hymnal', '찬숑가_(1920년).pdf', 1, [50, 50], '새찬송가가 아니라, 100여 년 전인 1920년에 나온 『찬숑가』의 표지예요 · 자료: 조선예수교서회 · 퍼블릭 도메인 · 위키미디어 공용', '붉은 천 표지에 ‘찬숑가’라고 쓴 제목 종이를 붙인 옛 책.'),
# 한국관광공사 공공누리 제1유형(한국관광콘텐츠랩). 파일 칸은 이름표, 사진 정보 주소는 아래 CRU에 따로 적어요.
('kl-yunhakja', '목포 유달산(정지훈)', None, [50, 50], '인물 사진이 아니라, 공생원이 있는 목포 유달산의 안개 낀 아침이에요 · 사진: 한국관광공사 정지훈 · 공공누리 제1유형 · 한국관광콘텐츠랩', '안개가 내려앉은 산봉우리에 정자가 서 있고 앞쪽에 푸른 나무가 우거진 세로 사진.'),
('aa-kimkichang', '청주_운보의 집 (11)', None, [60, 55], '작품이 아니라, 김기창이 말년을 보낸 청주 ‘운보의 집’ 한옥이에요 · 사진: 한국관광공사 · 공공누리 제1유형 · 한국관광콘텐츠랩', '정원 너머로 보이는 기와지붕 한옥과 꽃이 핀 화단.'),
('kl-sonyangwon', '여수_손양원목사 순교기념관 (2)', None, [45, 50], '인물 사진이 아니라, 손양원 목사가 한센병 환자들과 함께한 여수 애양원의 돌 예배당이에요 · 사진: 한국관광공사 · 공공누리 제1유형 · 한국관광콘텐츠랩', '가을 나무 너머로 보이는, 회색 돌로 쌓은 탑이 있는 예배당.'),
('kl-chimyeong', '전주_치명자산성지 (2)', None, [50, 55], '인물 사진이 아니라, 이순이·유중철 부부와 가족이 함께 묻힌 치명자산 성지의 무덤이에요 · 사진: 한국관광공사 · 공공누리 제1유형 · 한국관광콘텐츠랩', '숲속 언덕에 둥글게 솟은 풀 덮인 무덤과 그 뒤의 돌 십자가.'),
('kch-geumsan', '김제_금산교회 (2)', None, [45, 55], '1908년에 지은 ㄱ자 한옥 예배당이에요 · 사진: 한국관광공사 · 공공누리 제1유형 · 한국관광콘텐츠랩', '잔디밭 위에 선 기와지붕 한옥 예배당.'),
]
def page_url_raw(f):
    from urllib.parse import quote
    return 'https://commons.wikimedia.org/wiki/File:' + quote(f.replace(' ', '_'), safe="(),'!_-.~")

# 위키미디어 공용이 아닌 사진의 '사진 정보' 주소(한국관광공사 원본 파일). an-veggie는 그림 두 장 가운데 토마토 쪽으로 이어요.
CRU = {
    'an-veggie': page_url_raw('Tomate_rouge_grosse_hâtive_Vilmorin-Andrieux_1904.png'),
    'kl-yunhakja': 'https://tong.visitkorea.or.kr/cms/resource_photo/93/4129893_image2_1.jpg',
    'aa-kimkichang': 'https://tong.visitkorea.or.kr/cms/resource/81/3504581_image2_1.jpg',
    'kl-sonyangwon': 'https://tong.visitkorea.or.kr/cms/resource/79/3580979_image2_1.jpg',
    'kl-chimyeong': 'https://tong.visitkorea.or.kr/cms/resource/05/3529505_image2_1.jpg',
    'kch-geumsan': 'https://tong.visitkorea.or.kr/cms/resource/30/3560930_image2_1.jpg',
}
WAIT = []

def page_url(f):
    from urllib.parse import quote
    return 'https://commons.wikimedia.org/wiki/File:' + quote(f.replace(' ', '_'), safe="(),'!_-.~")

def cru_of(cid, f):
    return CRU.get(cid) or page_url(f)

if __name__ == '__main__':
    import json, sys
    ids = [x[0] for x in FIX]
    assert len(ids) == len(set(ids)), 'id 겹침'
    print(len(FIX), 'cards ready,', len(WAIT), 'waiting')
    if len(sys.argv) > 1 and sys.argv[1] == 'js':
        # 브라우저에서 내려받을 목록(JS 배열)
        print(json.dumps([[i, f, p] for i, f, p, *_ in FIX], ensure_ascii=False))
