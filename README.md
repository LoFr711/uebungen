# Inhalt
Programmieraufgaben aus den Vorlesungen 
- "Grundlagen der Informatik" (WiSe 22/23)
- "Algorithmen und Datenstrukturen" (SoSe 23)
- "Grundlagen informatischer Problemlösungen" (WiSe 24/25)
- "Einführung in die (symbolische) künstliche Intelligenz" (WiSe 24/25)
- "Einführung in die Theorie künstlicher Neuronaler Netze" (WiSe 24/25)

## Caesar-Chiffre
Enthält die zwei Funktionen, encipher() und decipher(), die die Großbuchstaben eines gegebenen Textes um n Stellen verschieben. 
Das Programm könnte ohne großen Aufwand so erweitert werden, dass auch kleine Buchstaben verschoben werden. Die main Funktion kann umgeschrieben werden, sodass man vom Programm gefragt wird ob man einen Text verschlüsseln oder entschlüsseln möchte. Aktuell gibt man bei encipher den Schlüssel vor - man könnte das so umändern, dass das Programm den Schlüssel generiert

## Magic Square
Ein magisches Quadrat der Seitenlänge (n x n) Matrix in der die Zahlen so angeordnet sind, dass in jeder Zeile und jeder Spalte die Summe der Zahlen gleich hoch ist. Das Programm ist eine Implementation eines Algorithmus der eine mögliche Darstellung des Quadrats für eine gegebene ungerade Zahl n berechnet. Eine Erweiterung des Programmes könnte zusätzlich einen Algorithmus für Quadrate mit gerader Kantenanzahl implementieren

## Rekursion
Das Programm berechnet für eingegebene natürliche Zahlen die Funktionen add() und mult() rekursiv. 

## Decorators
Decorators zeigt am Beispiel der Fibonacci Folgen, wie sich Laufzeiten von Python Programmen mithilfe von Decoratorn reduzieren lassen

## Sierpinsky
Erstellt mithilfe des Python Moduls "Turtle" das Sierpinsky Dreieck in eingegebener Rekursionstiefe. Der "Pfad" wird mithilfe des Lindenmayer - Systems berechnet

## Mandelbrot
Das Programm erstellt ein jpg des Mandelbrotes. Aktuell müssen Auflösung und Rekursionstiefe händisch im Code geändert werden. Eine Erweiterung des Programms könnte mehrere Mandelbrote in verschiedener Auflösung erstellen oder einen Zoom in einen  bestimmten Bildausschnitt implementieren

## Priority_Queue
Eine Prioritätswarteschlange ist eine Datenstruktur, die die Operationen die sie kann effizienter als der binäre Suchbaum durchführt. Sie wird zB für Djikstras  schnellsten Wege Algorithmus verwendet. Das Programm Priority_Queue erstellt eine Datenklasse Priority_Queue mit den gängigen Operationen. Die Datenklasse kann dann zB zur Wegesuche für einen Datensatz verwendet werden

## Star Maze
Erstellt in Zusammenarbeit mit Duong Nguyen und Alex Keller
Ein Star Maze stellt in dieser Aufgabe ein Labyrinth dar, für dass mit dem A Suchalgorithmus ein Weg zu einem Ziel gefunden werden soll. Ein Star Maze besteht aus einem Start 'S', mindestens einem Ziel 'F' und Wänden die mithilfe von '#' dargestellt werden.
Die heuristische Funktion berechnet die Manhatten Distanz zwischen einem Knoten und dem Ziel.

## Tuerme von Hanoi
Erstellt in Zusammenarbeit mit Duong Nguyen und Alex Keller
Die Tuerme von Hanoi ist ein Spiel mit dem Ziel einen Turm von Scheiben von einer Säule auf eine andere Säule zu bewegen. Hierbei darf pro Schritt immer nur eine Scheibe bewegt werden und Scheiben dürfen nur auf größere Scheiben oder freie Stellen gelegt werden.
Bei einer Erweiterung des Programmes würde es sich lohnen eine Klasse TuermeVonHanoi zu definieren auf die Funktionen als Klassenoperationen angewendet werden dürfen. Da die Tuerme von Hanoi keine Sackgassen und endliche Suchräume haben, könnte man einfach verschiedene Suchalgorithmen implementieren um sie miteinander zu vergleichen.
